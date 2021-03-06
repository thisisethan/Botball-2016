'''
module for wrapping all necessary wallaby functions

The fact I have to write this is ridiculous
'''

from ctypes import CDLL, c_int, c_short
from decorators import accepts, returns, cast_to

#CDLL assumes that all functions return a c_int
_wallaby = CDLL("libwallaby.so")


'''
BEGIN MOTOR FUNCTIONS

int get_motor_position_counter(int motor);

int gmpc(int motor);

void clear_motor_position_counter(int motor);

void cmpc(int motor);

int move_at_velocity(int motor, int velocity);

int mav(int motor, int velocity);

int move_to_position(int motor, int speed, int goal_pos);

int mtp(int motor, int speed, int goal_pos);

int move_relative_position(int motor, int speed, int delta_pos);

int mrp(int motor, int speed, int delta_pos);

int freeze(int motor);

int get_motor_done(int motor);

void block_motor_done(int motor);

void bmd(int motor);

int setpwm(int motor, int pwm);

int getpwm(int motor);

void fd(int motor);

void bk(int motor);

void motor(int motor, int percent);

void off(int motor);

void alloff();

void ao();

'''

@accepts(int)
@returns(int)
@cast_to(c_int)
def get_motor_position_counter(motor_num):
    '''gets motor position counter
    fill in section once we know what that means
    '''

    status = _wallaby.get_motor_position_counter(motor_num)
    return int(status)

@accepts(int)
@returns(int)
def gmpc(motor_num):
    '''
    shortened alias for get_motor_position_counter
    '''

    return get_motor_position_counter(motor_num)

@accepts(int)
@cast_to(c_int)
def clear_motor_position_counter(motor_num):
    '''
    clears the motor position counter
    '''

    _wallaby.clear_motor_position_counter(motor_num)

@accepts(int)
def cmpc(motor_num):
    '''
    shortened alias for clear_motor_position_counter
    '''
    clear_motor_position_counter(motor_num)

@accepts(int, int)
@cast_to(c_int, c_int)
def move_at_velocity(motor_num, velocity):
    '''
    moves the designated motor at velocity

    velocity is given in [TBD]
    '''

    _wallaby.move_at_velocity(motor_num, velocity)


@accepts(int, int)
def mav(motor_num, velocity):
    '''
    shortened alias for move_at_velocity
    '''
    move_at_velocity(motor_num, velocity)

@accepts(int, int, int)
@cast_to(c_int, c_int, c_int)
def move_to_position(motor_num, speed, goal_pos):
    '''
    moves the motor to a given position
    '''
    _wallaby.move_to_position(motor_num,
                              speed,
                              goal_pos)

@accepts(int, int, int)
@cast_to(c_int, c_int, c_int)
def mtp(motor_num, speed, goal_pos):
    '''
    shortened alias for move_to_position
    '''

    move_to_position(motor_num, speed, goal_pos)

@accepts(int, int, int)
@cast_to(c_int, c_int, c_int)
def move_relative_position(motor_num, speed, delta_pos):
    '''move motor to a relative position'''

    _wallaby.move_relative_position(motor_num, speed, delta_pos)

def mrp(motor_num, speed, delta_pos):
    '''shortened alias for move_relative_position'''
    move_relative_position(motor_num, speed, delta_pos)

@accepts(int)
@cast_to(c_int)
def freeze(motor_num):
    '''freezes the motor'''
    _wallaby.freeze(motor_num)

@accepts(int)
@returns(bool)
@cast_to(c_int)
def get_motor_done(motor_num):
    '''gets if the motor is done'''
    result = _wallaby.get_motor_done(motor_num)
    return bool(int(result))

@accepts(int)
@cast_to(c_int)
def block_motor_done(motor_num):
    '''block motor done'''
    _wallaby.block_motor_done(motor_num)

@accepts(int)
def bmd(motor_num):
    '''alias for block motor done'''
    block_motor_done(motor_num)

@accepts(int)
@cast_to(c_int)
def setpwm(motor_num, pwm):
    '''sets the pwm'''
    _wallaby.setpwm(motor_num, pwm)

@accepts(int)
@cast_to(c_int)
def getpwm(motor_num):
    '''gets the pwm'''
    _wallaby.getpwm(motor_num)

@accepts(int)
@cast_to(c_int)
def fd(motor_num):
    '''runs the motor forwards'''
    _wallaby.fd(motor_num)

@accepts(int)
@cast_to(c_int)
def bk(motor_num):
    '''runs the motor backwards'''
    _wallaby.bk(motor_num)

#insert more here

@accepts(int, int)
@cast_to(c_int, c_int)
def motor(motor_num, power_level):
    '''puts the specified motor to the specified power'''

    _wallaby.motor(motor_num, power_level)

@accepts(int)
@cast_to(c_int)
def off(motor_num):
    '''turns the specified motor off'''

    _wallaby.off(motor_num)

def ao():
    '''turns all motors off'''
    _wallaby.ao()

def all_off():
    '''turns all motors off'''
    ao()





'''
BEGIN ANALOG SENSOR FUNCTIONS

int analog(int port);

int analog8(int port);

int analog10(int port);

int analog12(int port);

int analog_et(int port);

void set_analog_pullup(int port, int pullup);

int get_analog_pullup(int port);
'''

@accepts(int)
@cast_to(c_int)
@returns(int)
def analog(port):
    '''gets the reading from the analog sensor at a port'''
    return int(_wallaby.analog(port))

@accepts(int)
@cast_to(c_int)
@returns(int)
def analog8(port):
    '''gets the 8 bit reading from the analog sensor at a port'''
    return int(_wallaby.analog8(port))

@accepts(int)
@cast_to(c_int)
@returns(int)
def analog10(port):
    '''gets the 10 bit reading from the analog sensor at a port'''
    return int(_wallaby.analog10(port))

@accepts(int)
@cast_to(c_int)
@returns(int)
def analog12(port):
    '''gets the 12 bit reading from the analog sensor at a port'''
    return int(_wallaby.analog12(port))

@accepts(int)
@cast_to(c_int)
@returns(int)
def analog_et(port):
    '''gets the reading from the ET sensor at a port'''
    return int(_wallaby.analog_et(port))

@accepts(int, int)
@cast_to(c_int, c_int)
def set_analog_pullup(port, pullup):
    '''sets the pullup for a port'''
    _wallaby.set_analog_pullup(port, pullup)

@accepts(int)
@cast_to(c_int)
@returns(int)
def get_analog_pullup(port):
    '''gets the pullup for a port'''
    return int(_wallaby.get_analog_pullup(port))

'''
BEGIN ACCELEROMETER FUNCTIONS

signed short accel_x();

signed short accel_y();

signed short accel_z();

int accel_calibrate();

'''

_wallaby.accel_x.restype = c_short

@returns(int)
def accel_x():
    '''gets the x value of the accelerometer'''
    return int(_wallaby.accel_x())

_wallaby.accel_y.restype = c_short

@returns(int)
def accel_y():
    '''gets the y value of the accelerometer'''
    return int(_wallaby.accel_y())

_wallaby.accel_z.restype = c_short

@returns(int)
def accel_z():
    '''gets the z value of the accelerometer'''
    return int(_wallaby.accel_z())

@returns(int)
def accel_calibrate():
    '''calibrates the accelerometer'''
    return int(_wallaby.accel_calibrate())

'''
BEGIN DIGITAL FUNCTIONS

int digital(int port);

void set_digital_value(int port, int value);

int get_digital_value(int port);

void set_digital_output(int port, int out);

int get_digital_output(int port);

int get_digital_pullup(int port);

void set_digital_pullup(int port, int pullup);
'''

@accepts(int)
@cast_to(c_int)
@returns(int)
def digital(port):
    '''returns the value of the digital port, either zero or one'''
    return int(_wallaby.digital(port))

@accepts(int, int)
@cast_to(c_int, c_int)
def set_digital_value(port, value):
    '''sets the digital value of a port'''
    _wallaby.set_digital_value(port, value)

@accepts(int)
@cast_to(c_int)
@returns(int)
def get_digital_value(port):
    '''gets the digital value at a port'''
    return int(_wallaby.get_digital_value(port))

@accepts(int, int)
@cast_to(c_int, c_int)
def set_digital_output(port, out):
    '''sets digital output'''
    _wallaby.set_digital_output(port, out)

@accepts(int)
@cast_to(c_int)
@returns(int)
def get_digital_output(port):
    '''gets digital output at a port'''
    return int(_wallaby.get_digital_output(port))

@accepts(int)
@cast_to(c_int)
@returns(int)
def get_digital_pullup(port):
    '''gets digital pullup'''
    return int(_wallaby.get_digital_pullup(port))

@accepts(int, int)
@cast_to(c_int, c_int)
def set_digital_pullup(port, pullup):
    '''sets digital pullup'''
    _wallaby.set_digital_pullup(port, pullup)


r'''
BEGIN CREATE FUNCTIONS

/*!
 * Waits to establish a connection to the create.
 * \blocksuntil A connection to a create is established
 * \return 0 on success
 * \see create_disconnect
 * \ingroup create
 */
 int create_connect();

/*!
 * Attempts to establish a connection to the create.
 * \return 1 if connection succeeded, 0 if connection failed
 * \see create_disconnect
 * \ingroup create
 */
 int create_connect_once();

/*!
 * Cleans up connection to the create.
 * \see create_connect
 * \ingroup create
 */
 void create_disconnect();


 void create_start();


 void create_passive();


 void create_safe();


 void create_full();


 void create_spot();


 void create_cover();


 void create_demo(int d);


 void create_cover_dock();


 int get_create_mode();


 int get_create_lbump();


 int get_create_rbump();


 int get_create_lwdrop();


 int get_create_cwdrop();


 int get_create_rwdrop();


 int get_create_wall();


 int get_create_lcliff();


 int get_create_lfcliff();


 int get_create_rfcliff();


 int get_create_rcliff();


 int get_create_llightbump();


 int get_create_lflightbump();


 int get_create_lclightbump();


 int get_create_rclightbump();


 int get_create_rflightbump();


 int get_create_rlightbump();


 int get_create_llightbump_amt();


 int get_create_rlightbump_amt();


 int get_create_lflightbump_amt();


 int get_create_lclightbump_amt();


 int get_create_rclightbump_amt();


 int get_create_rflightbump_amt();


 int get_create_vwall();


 int get_create_overcurrents();


 int get_create_infrared();


 int get_create_advance_button();


 int get_create_play_button();


 int get_create_normalized_angle();


 void set_create_normalized_angle(int angle);


 int get_create_total_angle();


 void set_create_total_angle(int angle);


 int get_create_distance();


 void set_create_distance(int dist);


 int get_create_battery_charging_state();


 int get_create_battery_voltage();


 int get_create_battery_current();


 int get_create_battery_temp();


 int get_create_battery_charge();


 int get_create_battery_capacity();


 int get_create_wall_amt();


 int get_create_lcliff_amt();


 int get_create_lfcliff_amt();


 int get_create_rfcliff_amt();


 int get_create_rcliff_amt();


 int get_create_bay_DI();


 int get_create_bay_AI();


 int get_create_song_number();


 int get_create_song_playing();


 int get_create_number_of_stream_packets();


 int get_create_requested_velocity();


 int get_create_requested_radius();


 int get_create_requested_right_velocity();


 int get_create_requested_left_velocity();


 void create_stop();


 void create_drive(int speed, int radius);


 void create_drive_straight(int speed);


 void create_spin_CW(int speed);


 void create_spin_CCW(int speed);


 void create_drive_direct(int l_speed, int r_speed);


 void create_spin_block(int speed, int angle);


 void create_advance_led(int on);


 void create_play_led(int on) ;


 void create_power_led(int color, int brightness);


 void create_digital_output(int bits);


 void create_pwm_low_side_drivers(int pwm2, int pwm1, int pwm0);


 void create_low_side_drivers(int pwm2, int pwm1, int pwm0);


 void create_load_song(int num);


 void create_play_song(int num);


 int create_read_block(char *data, int count);


 void create_write_byte(char byte);


 void create_clear_serial_buffer();

'''
