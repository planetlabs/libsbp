/*
 * Copyright (C) 2015 Swift Navigation Inc.
 * Contact: Fergus Noble <fergus@swift-nav.com>
 *
 * This source is subject to the license found in the file 'LICENSE' which must
 * be be distributed together with this source. All other rights reserved.
 *
 * THIS CODE AND INFORMATION IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
 * EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
 */

/*****************************************************************************
 * Automatically generated from piksi/yaml/
 * with generate.py at 2015-03-13 13:32:04.124636. Please do not hand edit!
 *****************************************************************************/

#ifndef LIBSBP_NAVIGATION_MESSAGES_H
#define LIBSBP_NAVIGATION_MESSAGES_H

#include "common.h"


/** GPS Time
  * GPS Time.
 */
#define SBP_MSG_GPS_TIME      0x0100
typedef struct __attribute__((packed)) {
  u16 wn;       /**< GPS week number [weeks] */
  u32 tow;      /**< GPS Time of Week rounded to the nearest ms [ms] */
  s32 ns;       /**< Nanosecond remainder of rounded tow [ns] */
  u8 flags;    /**< Status flags (reserved) */
} msg_gps_time_t;


/** Dilution of Precision
  * Dilution of Precision.
 */
#define SBP_MSG_DOPS          0x0206
typedef struct __attribute__((packed)) {
  u32 tow;     /**< GPS Time of Week [ms] */
  u16 gdop;    /**< Geometric Dilution of Precision [0.01] */
  u16 pdop;    /**< Position Dilution of Precision [0.01] */
  u16 tdop;    /**< Time Dilution of Precision [0.01] */
  u16 hdop;    /**< Horizontal Dilution of Precision [0.01] */
  u16 vdop;    /**< Vertical Dilution of Precision [0.01] */
} msg_dops_t;


/** Position in ECEF
  * Position solution in absolute Earth Centered Earth Fixed (ECEF)
 * coordinates.
 */
#define SBP_MSG_POS_ECEF      0x0200
typedef struct __attribute__((packed)) {
  u32 tow;         /**< GPS Time of Week [ms] */
  double x;           /**< ECEF X coordinate [m] */
  double y;           /**< ECEF Y coordinate [m] */
  double z;           /**< ECEF Z coordinate [m] */
  u16 accuracy;    /**< Position accuracy estimate [mm] */
  u8 n_sats;      /**< Number of satellites used in solution */
  u8 flags;       /**< Status flags */
} msg_pos_ecef_t;


/** Geodetic Position
  * Geodetic position solution.
 */
#define SBP_MSG_POS_LLH       0x0201
typedef struct __attribute__((packed)) {
  u32 tow;           /**< GPS Time of Week [ms] */
  double lat;           /**< Latitude [deg] */
  double lon;           /**< Longitude [deg] */
  double height;        /**< Height [m] */
  u16 h_accuracy;    /**< Horizontal position accuracy estimate [mm] */
  u16 v_accuracy;    /**< Vertical position accuracy estimate [mm] */
  u8 n_sats;        /**< Number of satellites used in solution */
  u8 flags;         /**< Status flags */
} msg_pos_llh_t;


/** Baseline in ECEF
  * Baseline in Earth Centered Earth Fixed (ECEF) coordinates.
 */
#define SBP_MSG_BASELINE_ECEF 0x0202
typedef struct __attribute__((packed)) {
  u32 tow;         /**< GPS Time of Week [ms] */
  s32 x;           /**< Baseline ECEF X coordinate [mm] */
  s32 y;           /**< Baseline ECEF Y coordinate [mm] */
  s32 z;           /**< Baseline ECEF Z coordinate [mm] */
  u16 accuracy;    /**< Position accuracy estimate [mm] */
  u8 n_sats;      /**< Number of satellites used in solution */
  u8 flags;       /**< Status flags */
} msg_baseline_ecef_t;


/** Baseline in NED
  * Baseline in local North East Down (NED) coordinates.
 */
#define SBP_MSG_BASELINE_NED  0x0203
typedef struct __attribute__((packed)) {
  u32 tow;           /**< GPS Time of Week [ms] */
  s32 n;             /**< Baseline North coordinate [mm] */
  s32 e;             /**< Baseline East coordinate [mm] */
  s32 d;             /**< Baseline Down coordinate [mm] */
  u16 h_accuracy;    /**< Horizontal position accuracy estimate [mm] */
  u16 v_accuracy;    /**< Vertical position accuracy estimate [mm] */
  u8 n_sats;        /**< Number of satellites used in solution */
  u8 flags;         /**< Status flags */
} msg_baseline_ned_t;


/** Velocity in ECEF
  * Velocity in Earth Centered Earth Fixed (ECEF) coordinates.
 */
#define SBP_MSG_VEL_ECEF      0x0204
typedef struct __attribute__((packed)) {
  u32 tow;         /**< GPS Time of Week [ms] */
  s32 x;           /**< Velocity ECEF X coordinate [mm/s] */
  s32 y;           /**< Velocity ECEF Y coordinate [mm/s] */
  s32 z;           /**< Velocity ECEF Z coordinate [mm/s] */
  u16 accuracy;    /**< Velocity accuracy estimate [mm/s] */
  u8 n_sats;      /**< Number of satellites used in solution */
  u8 flags;       /**< Status flags (reserved) */
} msg_vel_ecef_t;


/** Velocity in NED
  * Velocity in local North East Down (NED) coordinates.
 */
#define SBP_MSG_VEL_NED       0x0205
typedef struct __attribute__((packed)) {
  u32 tow;           /**< GPS Time of Week [ms] */
  s32 n;             /**< Velocity North coordinate [mm/s] */
  s32 e;             /**< Velocity East coordinate [mm/s] */
  s32 d;             /**< Velocity Down coordinate [mm/s] */
  u16 h_accuracy;    /**< Horizontal velocity accuracy estimate [mm/s] */
  u16 v_accuracy;    /**< Vertical velocity accuracy estimate [mm/s] */
  u8 n_sats;        /**< Number of satellites used in solution */
  u8 flags;         /**< Status flags (reserved) */
} msg_vel_ned_t;


#endif /* LIBSBP_NAVIGATION_MESSAGES_H */