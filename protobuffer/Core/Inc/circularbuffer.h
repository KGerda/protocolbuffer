/*
 * circularbuffer.h
 *
 *  Created on: Mar 24, 2025
 *      Author: Gerda
 */

#ifndef INC_CIRCULARBUFFER_H_
#define INC_CIRCULARBUFFER_H_

#include <stdio.h>
#include <string.h>
#include <stdint.h>
#include "stdbool.h"

#define BUFFER_LEN (1000)

void getdata_frombuffer(uint8_t data[],uint8_t len);
bool writedata_tobuffer(uint8_t data[],uint8_t len);



#endif /* INC_CIRCULARBUFFER_H_ */
