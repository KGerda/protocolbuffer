#include "circularbuffer.h"


extern uint8_t buffer[BUFFER_LEN];
volatile uint32_t writePtr = 0;
volatile uint32_t readPtr = 0;


void getdata_frombuffer(uint8_t ret_data[],uint8_t len)
{
		if(readPtr < writePtr)
		  {
            memcpy(ret_data,&buffer[readPtr],len);
			readPtr = readPtr+len;
		  }
		else if (readPtr > writePtr)
		  {
			uint32_t firstPart = BUFFER_LEN - readPtr;
	        if (len <= firstPart) // Ha elfér az egész adat a puffer végén
	        {
	            memcpy(ret_data, &buffer[readPtr], len);
	            readPtr += len;
	        }
	        else // Ha a len nagyobb, mint a maradék hely a puffer végén
	        {
	            memcpy(ret_data, &buffer[readPtr], firstPart);
	            memcpy(&ret_data[firstPart], &buffer[0], len - firstPart);
	            readPtr = len - firstPart;
	        }
		  }
}
	  

bool writedata_tobuffer(uint8_t data[],uint8_t len)
{
     // iras   *data
	if( (writePtr+len) < (BUFFER_LEN))
	{
		memcpy(&buffer[writePtr],data,len);
		writePtr+= len;
		return 1;

	}
	else
	{
		/* buffer első fele */
		uint32_t firstPart = BUFFER_LEN-writePtr;
		if(readPtr>len-firstPart)
		{
		memcpy(&buffer[writePtr],data,firstPart);
		/* Atcsordulas utani resz */
		memcpy(&buffer[0],&data[firstPart],len-firstPart);
		writePtr = len-firstPart;
		return 1;
		}
		else
			return 0;  //ekkor nem noveli datacountert
    }
}
