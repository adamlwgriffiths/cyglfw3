from math import sin, cos, atan2, pi
from random import random as rand
from OpenGL import GL as gl, GLU as glu
from cyglfw3.compatible import *

# *****************************************************************************
#  Title:   GLBoing
#  Desc:    Tribute to Amiga Boing.
#  Author:  Jim Brooks  <gfx@jimbrooks.org>
#           Original Amiga authors were R.J. Mical and Dale Luck.
#           GLFW conversion by Marcus Geelnard
#  Notes:   - 360' = 2*PI [radian]
#
#           - Distances between objects are created by doing a relative
#             Z translations.
#
#           - Although OpenGL enticingly supports alpha-blending,
#             the shadow of the original Boing didn't affect the color
#             of the grid.
#
#           - [Marcus] Changed timing scheme from interval driven to frame-
#             time based animation steps (which results in much smoother
#             movement)
#
#  History of Amiga Boing:
#
#  Boing was demonstrated on the prototype Amiga (codenamed "Lorraine") in
#  1985. According to legend, it was written ad-hoc in one night by
#  R. J. Mical and Dale Luck. Because the bouncing ball animation was so fast
#  and smooth, attendees did not believe the Amiga prototype was really doing
#  the rendering. Suspecting a trick, they began looking around the booth for
#  a hidden computer or VCR.
# ****************************************************************************

# ****************************************************************************
#  Various declarations and macros
# ****************************************************************************
RADIUS = 70.0
STEP_LONGITUDE = 22.50         # 22.5 makes 8 bands like original Boing
STEP_LATITUDE = 22.50

DIST_BALL = (RADIUS * 2.0 + RADIUS * 0.10)

VIEW_SCENE_DIST = (DIST_BALL * 3.0 + 200.0)   # distance from viewer to
                                              # middle of boing area
GRID_SIZE = (RADIUS * 4.50)                   # length (width) of grid
BOUNCE_HEIGHT = (RADIUS * 2.10)
BOUNCE_WIDTH = (RADIUS * 2.10)

SHADOW_OFFSET_X = -20.0
SHADOW_OFFSET_Y = 10.0
SHADOW_OFFSET_Z = 0.0

WALL_L_OFFSET = 0.0
WALL_R_OFFSET = 5.0

# Animation speed (50.0 mimics the original GLUT demo speed)
ANIMATION_SPEED = 50.0

# Maximum allowed delta time per physics iteration
MAX_DELTA_T = 0.020

#  Draw ball, or its shadow
DRAW_BALL = 0x0001
DRAW_BALL_SHADOW = 0x0010

# Set to true for debug output
BOING_DEBUG = False


# Vertex type
class Vertex(object):
    def __init__(self, x=None, y=None, z=None):
        x = x if x is not None else 0.0
        y = y if y is not None else 0.0
        z = z if z is not None else 0.0
        self.x, self.y, self.z = (x, y, z)

# Global vars
deg_rot_y = 0.0
deg_rot_y_inc = 2.0
ball_x = -RADIUS
ball_y = -RADIUS
ball_x_inc = 1.0
ball_y_inc = 2.0
drawBallHow = DRAW_BALL
t = dt = t_old = 0.0

# Persistent vars
colorToggle = False

# Random number generator
RAND_MAX = 4095


def my_range(start, stop=None, step=1.0):
    if stop is None:
        start, stop = 0.0, start
    current_count = start
    if step < 0:
        start, stop = stop, start
    elif step == 0:
        yield None
    while current_count <= stop:
        yield current_count
        current_count += step


# ****************************************************************************
#  Truncate a degree.
# ***************************************************************************
def TruncateDeg(deg):
    CAP_DEGREE = 360.0
    if (deg >= CAP_DEGREE):
        deg = deg - CAP_DEGREE
    return deg


# ****************************************************************************
#  Convert a degree (360-based) into a radian.
#  360' = 2 * PI
# ***************************************************************************
def deg2rad(deg):
    return deg / 360.0 * (2 * pi)


# ****************************************************************************
#  360' sin().
# ***************************************************************************
def sin_deg(deg):
    return sin(deg2rad(float(deg)))


# ****************************************************************************
#  360' cos().
# ***************************************************************************
def cos_deg(deg):
    return cos(deg2rad(float(deg)))


# ****************************************************************************
#  Compute a cross product (for a normal vector).
#
#  c = a x b
# ***************************************************************************
def CrossProduct(a, b, c):
    u1 = b.x - a.x
    u2 = b.y - a.y
    u3 = b.y - a.z

    v1 = c.x - a.x
    v2 = c.y - a.y
    v3 = c.z - a.z

    n = Vertex()
    n.x = u2 * v3 - v2 * v3
    n.y = u3 * v1 - v3 * u1
    n.z = u1 * v2 - v1 * u2
    return n


# ****************************************************************************
#  Calculate the angle to be passed to gluPerspective() so that a scene
#  is visible.  This function originates from the OpenGL Red Book.
#
#  Parms   : size
#            The size of the segment when the angle is intersected at "dist"
#            (ie at the outermost edge of the angle of vision).
#
#            dist
#            Distance from viewpoint to scene.
# ***************************************************************************
def PerspectiveAngle(size, dist):
    radTheta = 2.0 * atan2(size / 2.0, dist)
    degTheta = (180.0 * radTheta) / pi
    return degTheta


# ****************************************************************************
#  init()
# ***************************************************************************
def init():
    gl.glClearColor(0.550, 0.550, 0.550, 0.0)
    gl.glShadeModel(gl.GL_FLAT)


# ****************************************************************************
#  display()
# ***************************************************************************
def display():
    global drawBallHow, DRAW_BALL_SHADOW, DRAW_BALL

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glPushMatrix()

    drawBallHow = DRAW_BALL_SHADOW
    DrawBoingBall()

    DrawGrid()

    drawBallHow = DRAW_BALL
    DrawBoingBall()

    gl.glPopMatrix()
    gl.glFlush()


# ****************************************************************************
#  reshape()
# ***************************************************************************
def reshape(window, w, h):
    global RADIUS, VIEW_SCENE_DIST

    gl.glViewport(0, 0, w, h)

    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()

    glu.gluPerspective(PerspectiveAngle(RADIUS * 2, 200),
                       float(w)/h,
                       1.0,
                       VIEW_SCENE_DIST)

    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()

    glu.gluLookAt(0.0, 0.0, VIEW_SCENE_DIST,   # eye
                  0.0, 0.0, 0.0,               # center of vision
                  0.0, -1.0, 0.0)              # up vector


def key_callback(window, key, scancode, action, mods):
    if (key == GLFW_KEY_ESCAPE and action == GLFW_PRESS):
        glfwSetWindowShouldClose(window, gl.GL_TRUE)


# ****************************************************************************
#  Draw the Boing ball.
#
#  The Boing ball is sphere in which each facet is a rectangle.
#  Facet colors alternate between red and white.
#  The ball is built by stacking latitudinal circles.  Each circle is composed
#  of a widely-separated set of points, so that each facet is noticably large.
# ***************************************************************************
def DrawBoingBall():
    global DIST_BALL, deg_rot_y, deg_rot_y_inc, ANIMATION_SPEED, drawBallHow, \
        DRAW_BALL_SHADOW, SHADOW_OFFSET_X, SHADOW_OFFSET_Y, SHADOW_OFFSET_Z, \
        STEP_LONGITUDE, dt, MAX_DELTA_T

    gl.glPushMatrix()
    gl.glMatrixMode(gl.GL_MODELVIEW)

    # Another relative Z translation to separate objects.
    gl.glTranslatef(0.0, 0.0, DIST_BALL)

    # Update ball position and rotation (iterate if necessary)
    dt_total = dt
    while(dt_total > 0.0):
        dt2 = dt_total
        if dt_total > MAX_DELTA_T:
            dt2 = MAX_DELTA_T
        dt_total -= dt2
        BounceBall(dt2)
        new_rot = deg_rot_y + deg_rot_y_inc*(float(dt2)*ANIMATION_SPEED)
        deg_rot_y = TruncateDeg(new_rot)

    # Set ball position
    gl.glTranslatef(ball_x, ball_y, 0.0)

    # Offset the shadow.
    if (drawBallHow == DRAW_BALL_SHADOW):
        gl.glTranslatef(SHADOW_OFFSET_X, SHADOW_OFFSET_Y, SHADOW_OFFSET_Z)

    # Tilt the ball.
    gl.glRotatef(-20.0, 0.0, 0.0, 1.0)

    # Continually rotate ball around Y axis.
    gl.glRotatef(deg_rot_y, 0.0, 1.0, 0.0)

    # Set OpenGL state for Boing ball.
    gl.glCullFace(gl.GL_FRONT)
    gl.glEnable(gl.GL_CULL_FACE)
    gl.glEnable(gl.GL_NORMALIZE)

    # Build a faceted latitude slice of the Boing ball,
    # stepping same-sized vertical bands of the sphere.
    for lon_deg in my_range(0, 180, STEP_LONGITUDE):
        if lon_deg == 180:
            break
        # Draw a latitude circle at this longitude.
        DrawBoingBallBand(lon_deg, lon_deg + STEP_LONGITUDE)

    gl.glPopMatrix()


# ****************************************************************************
#  Bounce the ball.
# ***************************************************************************
def BounceBall(delta_t):
    global BOUNCE_WIDTH, WALL_R_OFFSET, BOUNCE_HEIGHT, WALL_L_OFFSET, \
        RAND_MAX, ANIMATION_SPEED, ball_x, ball_y, deg_rot_y_inc, ball_x_inc, \
        ball_y_inc

    # Bounce on walls
    if (ball_x > (BOUNCE_WIDTH/2 + WALL_R_OFFSET)):
        ball_x_inc = -0.50 - 0.750 * rand() / RAND_MAX
        deg_rot_y_inc = -deg_rot_y_inc

    if (ball_x < -(BOUNCE_HEIGHT/2 + WALL_L_OFFSET)):
        ball_x_inc = 0.50 + 0.750 * rand() / RAND_MAX
        deg_rot_y_inc = -deg_rot_y_inc

    # Bounce on floor / roof
    if (ball_y > BOUNCE_HEIGHT/2):
        ball_y_inc = -0.750 - 1.0 * rand() / RAND_MAX

    if (ball_y < -BOUNCE_HEIGHT/2*0.85):
        ball_y_inc = 0.750 + 1.0 * rand() / RAND_MAX

    # Update ball position
    ball_x += ball_x_inc * (float(delta_t)*ANIMATION_SPEED)
    ball_y += ball_y_inc * (float(delta_t)*ANIMATION_SPEED)

    # Simulate the effects of gravity on Y movement.

    if (ball_y_inc < 0):
        sign = -1.0
    else:
        sign = 1.0

    deg = (ball_y + BOUNCE_HEIGHT/2) * 90 / BOUNCE_HEIGHT
    if (deg > 80):
        deg = 80
    if (deg < 10):
        deg = 10

    ball_y_inc = sign * 4.0 * float(sin_deg(deg))


# ****************************************************************************
#  Draw a faceted latitude band of the Boing ball.
#
#  Parms:   long_lo, long_hi
#           Low and high longitudes of slice, resp.
# ***************************************************************************
def DrawBoingBallBand(long_lo, long_hi):
    global STEP_LATITUDE, DRAW_BALL_SHADOW, drawBallHow, RADIUS, \
        STEP_LONGITUDE, BOING_DEBUG, colorToggle

    vert_ne = Vertex()          # "ne" means north-east, so on
    vert_nw = Vertex()
    vert_sw = Vertex()
    vert_se = Vertex()
    vert_norm = Vertex()
    vert_names = ["ne", "nw", "sw", "se"]
    verts = [vert_ne, vert_nw, vert_sw, vert_se]

    # Iterate thru the points of a latitude circle.
    # A latitude circle is a 2D set of X,Z points.
    for lat_deg in my_range(0, 360-STEP_LATITUDE, STEP_LATITUDE):
        # Color this polygon with red or white.
        if (colorToggle is False):
            gl.glColor3f(0.80, 0.10, 0.10)
            colorToggle = True
        else:
            gl.glColor3f(0.950, 0.950, 0.950)
            colorToggle = False

        # Change color if drawing shadow.
        if (drawBallHow == DRAW_BALL_SHADOW):
            gl.glColor3f(0.350, 0.350, 0.350)

        # Assign each Y
        vert_ne.y = vert_nw.y = float(cos_deg(long_hi)) * RADIUS
        vert_sw.y = vert_se.y = float(cos_deg(long_lo)) * RADIUS

        # Assign each X,Z with sin,cos values scaled by latitude radius
        #  indexed by longitude.  Eg, long=0 and long=180 are at the
        #  poles, so zero scale is sin(longitude) while long=90
        #  (sin(90)=1) is at equator.
        cos_matrix = {vert_ne: (0, 1),
                      vert_nw: (1, 1),
                      vert_se: (0, 0),
                      vert_sw: (1, 0)}
        for vert in verts:
            new_lat = lat_deg + STEP_LATITUDE * cos_matrix[vert][0]
            new_lon = long_lo + STEP_LONGITUDE * cos_matrix[vert][1]
            vert.x = cos_deg(new_lat) * (RADIUS * sin_deg(new_lon))
            vert.z = sin_deg(new_lat) * (RADIUS * sin_deg(new_lon))

        # Draw the facet.
        gl.glBegin(gl.GL_QUADS)

        vert_norm = CrossProduct(vert_ne, vert_nw, vert_sw)
        gl.glNormal3f(vert_norm.x, vert_norm.y, vert_norm.z)

        for vert in verts:
            gl.glVertex3f(vert.x, vert.y, vert.z)

        gl.glEnd()

        if BOING_DEBUG:
            print("-"*79)
            lat_lon_lon = (lat_deg, long_lo, long_hi)
            print("lat = %f  long_lo = %f  long_hi = %f" % lat_lon_lon)
            for name, vert in zip(vert_names, verts):
                print("%s: %.8f | %.8f | %.8f" % (name, vert.x, vert.y, vert.z))

    # Toggle color so that next band will opposite red/white colors than
    #  this one.
    colorToggle = True if colorToggle is False else False


# ****************************************************************************
#  Draw the purple grid of lines, behind the Boing ball.
#  When the Workbench is dropped to the bottom, Boing shows 12 rows.
# ***************************************************************************
def DrawGrid():
    global GRID_SIZE, DIST_BALL

    row = col = 0
    rowTotal = 8                   # must be divisible by 2
    colTotal = rowTotal             # must be same as rowTotal
    widthLine = 2.0                 # should be divisible by 2
    sizeCell = GRID_SIZE / rowTotal
    z_offset = -40.0
    xl = xr = 0.0
    yt = yb = 0.0

    gl.glPushMatrix()
    gl.glDisable(gl.GL_CULL_FACE)

    # Another relative Z translation to separate objects.
    gl.glTranslatef(0.0, 0.0, DIST_BALL)

    # Draw vertical lines (as skinny 3D rectangles).
    for col in my_range(0, colTotal):
        # Compute co-ords of line.

        xl = -GRID_SIZE / 2 + col * sizeCell
        xr = xl + widthLine

        yt = GRID_SIZE / 2
        yb = -GRID_SIZE / 2 - widthLine

        gl.glBegin(gl.GL_POLYGON)

        gl.glColor3f(0.60, 0.10, 0.60)        # purple

        gl.glVertex3f(xr, yt, z_offset)       # NE
        gl.glVertex3f(xl, yt, z_offset)       # NW
        gl.glVertex3f(xl, yb, z_offset)       # SW
        gl.glVertex3f(xr, yb, z_offset)       # SE

        gl.glEnd()

    # Draw horizontal lines (as skinny 3D rectangles).
    for row in my_range(0, rowTotal):
        # Compute co-ords of line.
        yt = GRID_SIZE / 2 - row * sizeCell
        yb = yt - widthLine

        xl = -GRID_SIZE / 2
        xr = GRID_SIZE / 2 + widthLine

        gl.glBegin(gl.GL_POLYGON)

        gl.glColor3f(0.60, 0.10, 0.60)        # purple

        gl.glVertex3f(xr, yt, z_offset)       # NE
        gl.glVertex3f(xl, yt, z_offset)       # NW
        gl.glVertex3f(xl, yb, z_offset)       # SW
        gl.glVertex3f(xr, yb, z_offset)       # SE

        gl.glEnd()

    gl.glPopMatrix()


# ======================================================================*
#  main()
# ======================================================================
if __name__ == "__main__":
    from sys import exit
    # Init GLFW
    if not glfwInit():
        exit(1)

    glfwWindowHint(GLFW_DEPTH_BITS, 16)

    window = glfwCreateWindow(400, 400, "Boing (classic Amiga demo)")
    if not window:
        glfwTerminate()
        exit(1)

    glfwSetFramebufferSizeCallback(window, reshape)
    glfwSetKeyCallback(window, key_callback)

    glfwMakeContextCurrent(window)
    glfwSwapInterval(1)

    width, height = glfwGetFramebufferSize(window)
    reshape(window, width, height)

    glfwSetTime(0.0)

    init()

    # Main loop
    while 1:
        # Timing
        t = glfwGetTime()
        dt = t - t_old
        t_old = t

        # Draw one frame
        display()

        # Swap buffers
        glfwSwapBuffers(window)
        glfwPollEvents()

        # Check if we are still running
        if (glfwWindowShouldClose(window)):
            break

    glfwTerminate()
    exit(0)