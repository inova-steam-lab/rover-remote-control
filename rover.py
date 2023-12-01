import caninos_sdk as k9

class Rover:
    __is_moving = False

    def __load_pwm_engine(self):
        ''' Habilita PWM '''

        time_count = 1

        while time_count <= 4:
            self.labrador.pin5.enable_pwm(
                alias="P1", freq=25, duty_cycle=0.1*time_count)
            self.labrador.pin15.enable_pwm(
                alias="P3", freq=25, duty_cycle=0.1*time_count)
            self.labrador.pin3.enable_pwm(
                alias="P2", freq=25, duty_cycle=0.1*time_count)
            self.labrador.pin13.enable_pwm(
                alias="P4", freq=25, duty_cycle=0.1*time_count)
            time_count = time_count+1

    def __init__(self) -> None:
        self.labrador = k9.Labrador()
        self.__load_pwm_engine()

    def move_forward(self):
        ''' Move o rover para frente '''
        if not self.__is_moving:
            self.labrador.P1.pwm.start()
            self.labrador.P3.pwm.start()
            self.labrador.P2.pwm.stop()
            self.labrador.P4.pwm.stop()

            self.__is_moving = True
        print("Movendo...")

    def move_backward(self):
        ''' Retrocede o rover '''

        if not self.__is_moving:
            self.labrador.P1.pwm.stop()
            self.labrador.P3.pwm.stop()
            self.labrador.P2.pwm.start()
            self.labrador.P4.pwm.start()

            self.__is_moving = True
        print("Retrocedendo...")

    def move_left(self):
        ''' Vira o rover para esquerda '''
        if not self.__is_moving:
            self.labrador.P1.pwm.stop()
            self.labrador.P3.pwm.start()
            self.labrador.P2.pwm.start()
            self.labrador.P4.pwm.stop()

            self.__is_moving = True
        print("Virando para a esquerda...")

    def move_right(self):
        ''' Move o rover para a direita '''

        if not self.__is_moving:
            self.labrador.P1.pwm.start()
            self.labrador.P3.pwm.stop()
            self.labrador.P2.pwm.stop()
            self.labrador.P4.pwm.start()

            self.__is_moving = True
        print("Virando para a direita...")

    def stop(self):
        '''Para o rover '''
        self.labrador.P1.pwm.stop()
        self.labrador.P3.pwm.stop()
        self.labrador.P2.pwm.stop()
        self.labrador.P4.pwm.stop()

        self.__is_moving = False

        print('Parando')
