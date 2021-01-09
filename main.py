volume = 0
light2 = 0
led.enable(False)
light3 = 0

def on_forever():
    global light2, volume, light3
    light2 = smarthome.read_light_intensity(AnalogPin.P3)
    light3 = smarthome.read_light_intensity(AnalogPin.P3)
    if light2 < 20:
        volume = smarthome.read_noise(AnalogPin.P2)
        if volume < 70:
            neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB).show_color(neopixel.colors(NeoPixelColors.WHITE))
            basic.pause(1000)
            neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGBW).show_color(neopixel.colors(NeoPixelColors.ORANGE))
            basic.pause(1000)
            neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB).show_color(neopixel.colors(NeoPixelColors.INDIGO))
            basic.pause(1000)
            neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB).show_color(neopixel.colors(NeoPixelColors.YELLOW))
            basic.pause(2000)
            neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB).show_color(neopixel.colors(NeoPixelColors.BLUE))
        else:
            BH1750.off()
basic.forever(on_forever)
