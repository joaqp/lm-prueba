#include <stdint.h>
#include <string.h>
#include <msg.hpp>

class B {
public:
B(string m): _msg(m){}
~B{}

void init(){
    msg::init(m);
}
void fsm(){
    switch(_state){
        case SALUDO:
        if(m=='hola')
        {
            hola();
            _state=IDENTIFICACION;
        }
        break;
        case IDENTIFICACION:
        if(reconocer(m)==1){
            ok();
            _state=PASS;
        }else{
            error();
        }
        break;
        case PASS:
        if(pass(m)==1){
            pass();
        }else{
            error();
        }
        break;
    }


}


private:

string msg;
enum class state{
SALUDO,
IDENTIFICACION,
PASS
};

void hola(){msg::hola(_msg);}
void error(){msg::error(_msg);}
void ok(){msg::ok(_msg);}
bool reconocer(){msg::reconocer(_msg);}
bool pass(){msg::pass(_msg);}

};
