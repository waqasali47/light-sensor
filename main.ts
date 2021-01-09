let volume = 0
let light2 = 0
led.enable(false)
basic.forever(function () {
    light2 = smarthome.ReadLightIntensity(AnalogPin.P3)
    if (light2 < 20) {
        volume = smarthome.ReadNoise(AnalogPin.P2)
        if (volume < 70) {
            neopixel.create(DigitalPin.P3, 1, NeoPixelMode.RGB).showColor(neopixel.colors(NeoPixelColors.White))
            basic.pause(1000)
            neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGBW).showColor(neopixel.colors(NeoPixelColors.Orange))
            basic.pause(1000)
            neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB).showColor(neopixel.colors(NeoPixelColors.Indigo))
            basic.pause(1000)
            neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB).showColor(neopixel.colors(NeoPixelColors.Yellow))
            basic.pause(2000)
            neopixel.create(DigitalPin.P1, 1, NeoPixelMode.RGB).showColor(neopixel.colors(NeoPixelColors.Blue))
        }
    }
})
