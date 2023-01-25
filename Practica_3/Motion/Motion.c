/*
 * Motion.c
 *
 *  Created on: 28 nov. 2021
 *      Author: jorge
 */

#include <string.h>
#include <stdio.h>
#include "sl_i2cspm_instances.h"
#include "sl_sleeptimer.h"
#include "sl_imu.h"
#include "sl_sensor_imu.h"



void initMotion(void){
  sl_sensor_imu_init();
  sl_sensor_imu_enable(true);
  sl_sensor_imu_calibrate();


}

void getMotion(void){

  int16_t ovec[3];
  int16_t avec[3];
  sl_status_t sc;
  sc = sl_sensor_imu_get(ovec, avec);
        if (SL_STATUS_OK == sc) {
          //app_log_info("IMU: ORI : %04d,%04d,%04d", ovec[0], ovec[1], ovec[2]);
          //printf("ORI : %04d;%04d;%04d", ovec[0], ovec[1], ovec[2]);
            printf("%04d;%04d;%04d;%04d;%04d;%04d", ovec[0], ovec[1], ovec[2], avec[0], avec[1], avec[2]);
          //printf("\r\n");
          //sl_sleeptimer_delay_millisecond(1000);
          //printf("ACC : %04d;%04d;%04d", avec[0], avec[1], avec[2]);
          printf("\r\n");
          //sl_sleeptimer_delay_millisecond(1000);
          //app_log_nl();
          //app_log_info("IMU: ACC : %04d,%04d,%04d", avec[0], avec[1], avec[2]);
          //app_log_nl();

        }
        sl_sensor_imu_deinit();

}
