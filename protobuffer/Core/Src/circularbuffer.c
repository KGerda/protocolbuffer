#include "circularbuffer.h"

extern uint8_t buffer[BUFFER_LEN];
volatile uint32_t writePtr = 0;
volatile uint32_t readPtr = 0;

void getdata_frombuffer(uint8_t ret_data[], uint8_t len) {
	if (readPtr < writePtr) {
		memcpy(ret_data, &buffer[readPtr], len);
		readPtr = readPtr + len;
	} else if (readPtr > writePtr) {
		uint32_t firstPart = BUFFER_LEN - readPtr;
		/*If the data fits to the buffer*/
		if (len <= firstPart) {
			memcpy(ret_data, &buffer[readPtr], len);
			readPtr += len;
		}
		/*If len is larger than the remaining space at the end of the buffer*/
		else {
			memcpy(ret_data, &buffer[readPtr], firstPart);
			memcpy(&ret_data[firstPart], &buffer[0], len - firstPart);
			readPtr = len - firstPart;
		}
	}
}

bool writedata_tobuffer(uint8_t data[], uint8_t len) {
	if ((writePtr + len) < (BUFFER_LEN)) {
		/*always have one space (2 bytes) empty*/
		if (writePtr + len == readPtr)
			/*Not increase datacounter*/
			return 0;
		memcpy(&buffer[writePtr], data, len);
		writePtr += len;
		return 1;

	} else {
		/* First part of the data*/
		uint32_t firstPart = BUFFER_LEN - writePtr;
		if (readPtr > len - firstPart) {
			memcpy(&buffer[writePtr], data, firstPart);
			/* Back part of the stream */
			memcpy(&buffer[0], &data[firstPart], len - firstPart);
			writePtr = len - firstPart;
			return 1;
		} else
			/*Not increase datacounter*/
			return 0;
	}
}
