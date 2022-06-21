#include <led.hpp>
#include <stdint.h>

class blink {
    public:
     explicit blink(uint8_t l, uint32_t &count): _led(l), _count(_count) {}
     ~blink{}

     void init (){
        led::init(l);
    }

     void fsm(){
        switch(_state){
            case ON:
            if(_count<=0){
            off();
            _state=OFF;
            }else if (count>0){
                _state=ON;
            }
            break;
            case OFF:
            if(_count<=0){
                on();
                _state=ON;
            }else if (count>0){
                _state=OFF;
            }
            
            break;
            default:
            init();
        }
     
     }
     private:

     uint8_t _led;
     int32_t count;
     enum class _state{
        ON,
        OFF
     };

     void on  (){led::on(_led);}

     static constexpr uint32_t t_on= 300;
     static constexpr uint32_t t_off= 300;

};