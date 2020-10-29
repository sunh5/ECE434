// Made by Haoxuan Sun, 10/29/2020
#include <stdint.h>
#include <pru_cfg.h>
#include "resource_table_empty.h"
// #include "prugpio.h"

#define GPIO3 0x481AE000
#define GPIO_CLEARDATAOUT 0x190
#define GPIO_SETDATAOUT 0x194
#define P9_27 (1<<19)
unsigned int volatile * const GPIO3_CLEAR = (unsigned int *) (GPIO3 + GPIO_CLEARDATAOUT);
unsigned int volatile * const GPIO3_SET = (unsigned int *) (GPIO3 + GPIO_SETDATAOUT);

volatile register unsigned int __R30;
volatile register unsigned int __R31;

void main(void) {
	int i;

	// uint32_t *gpio3 = (uint32_t *)GPIO3;
	
	/* Clear SYSCFG[STANDBY_INIT] to enable OCP master port */
	CT_CFG.SYSCFG_bit.STANDBY_INIT = 0;

	for(i=0; i<10000000000000000; i++) {
		*GPIO3_SET   = P9_31;	// The the P9_31 on

		__delay_cycles(0);    	// Wait 0 second

		*GPIO3_CLEAR = P9_27;

		__delay_cycles(0); 

	}
	__halt();
}

// Turns off triggers
// #pragma DATA_SECTION(init_pins, ".init_pins")
// #pragma RETAIN(init_pins)
// const char init_pins[] =  
// 	"/sys/class/leds/beaglebone:green:usr3/trigger\0none\0" \
// 	"\0\0";
	