from abc import ABC, abstractmethod

# Interfaz
class ISwitchable(ABC):
    def turn_on(self) -> None:
        pass

    def turn_off(self) -> None:
        pass

# Interfaz
class ITemperatureRegulatable(ABC):
    @abstractmethod
    def set_temperature(self, temperature : int) -> None:
        pass

# Clase que llama a la interfaz
class SmartLight(ISwitchable):
    # Funcion que enciende la luz
    def turn_off(self):
        print(f"Turning light OFF")
    
    # Funcion que apaga la luz
    def turn_on(self):
        print(f"Turning light ON")

# Clase que llama a la interfaz
class SmartTemperature(ISwitchable, ITemperatureRegulatable):
    def turn_off(self):
        print(f"Turning light OFF")
    
    def turn_on(self):
        print(f"Turning light ON")
    
    # Funcion que setea la temperatura
    def set_temperature(self, temperature : int):
        print(f"Setting temperature {temperature}")

# Modo de uso

SmartLight = SmartLight()
SmartLight.turn_off()
SmartLight.turn_on()

SmartTherm = SmartTemperature()
SmartTherm.turn_off()
SmartTherm.turn_on()
SmartTherm.set_temperature(10)