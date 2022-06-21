#include <stdint.h>
#include <Button.hpp>

class Antirrebote{
    public:
    explicit Antirrebote(uint8_t boton, uint32_t &count): _Button(boton), _timer(count){}
    ~Antirrebote {}

    void init(){
        Button::init(boton);
    }
    
    void fsm(){
        switch(_state){
            case SUELTO:
            if(boton==1){
                ventana_desc();
                _state=VENTANA_DESC;
                count=0;
            }
            break;
            case VENTANA_DESC:
            if(count=50){ //asumo que esta seteado
            presionado();
            _state=PRESIOANADO;
            }
            break;
            case PRESIONADO:
            if(boton==0){
                ventana_asce();
                _state=VENTANA_ASCE;
                count=0;
            }
    
            break;
            case VENTANA_ASCE:
            if(count=50){
                suelto();
                _state=SUELTO;
            }
            
            break;
            default:
            init();

        }


    }

    private:

    uint8_t _button;
    int32_t count;
     enum class _state{
        SUELTO,
        VENTANA_DESC,
        PRESIONADO,
        VENTANA_ASCE
     };

     void suelto (){button::suelto(_button);}
     void ventana_desc (){button::ventana_desc(_button);}
     void presionado (){button::presionado(_button);}
     void ventana_asce(){button::ventana_aesce(_button);}

};