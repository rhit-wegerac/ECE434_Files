#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
#include "prugpio.h"

volatile register unsigned int __R30;
volatile register unsigned int __R31;

#define P9_31	(0x1<<14)

void main(void) {
	int i;

	uint32_t *gpio1 = (uint32_t *)GPIO1;
	uint32_t *gpio3 = (uint32_t *)GPIO3;
	uint32_t *gpio0 = (uint32_t *)GPIO0;
	
	//uint32_t gpio = P9_31;	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */

	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	//for(i=0; i<50; i++) {
	while(1){
		//gpio1[GPIO_SETDATAOUT]   = USR3;	// The the USR3 LED on
		gpio3[GPIO_SETDATAOUT]   = P9_31;
		
		//__R30 |= gpio;
		
		//__delay_cycles(500000000/5);    	// Wait 1/2 second
		__delay_cycles(0); 

		//gpio1[GPIO_CLEARDATAOUT] = USR3;
		gpio3[GPIO_CLEARDATAOUT] = P9_31;
		
		//__R30 &= ~gpio;
		
		//__delay_cycles(500000000/5); 
		__delay_cycles(0); 

	}
	__halt();
}

// // Turns off triggers
// #pragma DATA_SECTION(init_pins, ".init_pins")
// #pragma RETAIN(init_pins)
// const char init_pins[] =  
// 	"/sys/class/leds/beaglebone:green:usr3/trigger\0none\0" \
// 	"\0\0";
// // const char init_pins[] =  
// // 	"/sys/class/leds/beaglebone:green:usr3/trigger\0none\0" \
// // 	"/sys/class/gpio/export\0 110\0" \
// // 	"/sys/class/gpio/gpio110/direction\0out\0" \
// // 	"\0\0";
