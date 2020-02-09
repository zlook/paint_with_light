#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
#include <avr/power.h> // Required for 16 MHz Adafruit Trinket
#endif

//#define PIN        7 // On Trinket or Gemma, suggest changing this to 1

Adafruit_NeoPixel pixels(26, 7, NEO_GRB + NEO_KHZ800);

char *FONT_LIST[] = {"00000001000233200000000000", "00000444445555555520000000", "00000444444555555555000000", "00004440044653755755520000", "00003440040457665772552000", "00077144404016767773255000", "00377714441111576773225500", "00777666006776556773222520", "03777666006776657773222350", "07776666007776755773222250", "07776661027766755773222252", "07766560027767755773222233", "27765560027777555773222225", "27765560027777555773222225", "27766560027777555773222225", "07776560007763555573222233", "07776661007766755573222252", "07776661007776355573222250", "00777666006776657773222350", "00777766401311756773222500", "00077744444111576773225300", "00037444044113765577255000", "00002440040477655577550000", "00000440044777555555300000", "00000444441755555552000000", "00000044445555555200000000", "00000000000000000000000000"};

void setup()
{
#if defined(__AVR_ATtiny85__) && (F_CPU == 16000000)
  clock_prescale_set(clock_div_1);
#endif

  pixels.begin(); // INITIALIZE NeoPixel strip object (REQUIRED)
  Serial.begin(9600);
}

void loop()
{
  Serial.println("< start loop >");
  for (int i = 0; i < int(sizeof(FONT_LIST) / sizeof(FONT_LIST[0])); ++i)
  {
    pixels.clear(); // Set all pixel colors to 'off'

    //遍历字符串
    for (int j = 0; j < 26; j++)
    {
      if (FONT_LIST[i][j] == '0')
      {
        pixels.setPixelColor(j, pixels.Color(247, 249, 245));
      }
      if (FONT_LIST[i][j] == '1')
      {
        pixels.setPixelColor(j, pixels.Color(102, 79, 53));
      }
      if (FONT_LIST[i][j] == '2')
      {
        pixels.setPixelColor(j, pixels.Color(174, 221, 250));
      }
      if (FONT_LIST[i][j] == '3')
      {
        pixels.setPixelColor(j, pixels.Color(105, 194, 236));
      }
      if (FONT_LIST[i][j] == '4')
      {
        pixels.setPixelColor(j, pixels.Color(229, 181, 69));
      }
      if (FONT_LIST[i][j] == '5')
      {
        pixels.setPixelColor(j, pixels.Color(10, 163, 243));
      }
      if (FONT_LIST[i][j] == '6')
      {
        pixels.setPixelColor(j, pixels.Color(15, 75, 126));
      }
      if (FONT_LIST[i][j] == '7')
      {
        pixels.setPixelColor(j, pixels.Color(33, 200, 248));
      }
    }

    pixels.show(); // Send the updated pixel colors to the hardware.
    delay(50);
  }
  delay(2000);
}
