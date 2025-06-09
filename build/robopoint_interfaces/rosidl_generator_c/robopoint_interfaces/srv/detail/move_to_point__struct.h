// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robopoint_interfaces:srv/MoveToPoint.idl
// generated code does not contain a copyright notice

#ifndef ROBOPOINT_INTERFACES__SRV__DETAIL__MOVE_TO_POINT__STRUCT_H_
#define ROBOPOINT_INTERFACES__SRV__DETAIL__MOVE_TO_POINT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/MoveToPoint in the package robopoint_interfaces.
typedef struct robopoint_interfaces__srv__MoveToPoint_Request
{
  float x;
  float y;
  float z;
} robopoint_interfaces__srv__MoveToPoint_Request;

// Struct for a sequence of robopoint_interfaces__srv__MoveToPoint_Request.
typedef struct robopoint_interfaces__srv__MoveToPoint_Request__Sequence
{
  robopoint_interfaces__srv__MoveToPoint_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robopoint_interfaces__srv__MoveToPoint_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/MoveToPoint in the package robopoint_interfaces.
typedef struct robopoint_interfaces__srv__MoveToPoint_Response
{
  uint8_t structure_needs_at_least_one_member;
} robopoint_interfaces__srv__MoveToPoint_Response;

// Struct for a sequence of robopoint_interfaces__srv__MoveToPoint_Response.
typedef struct robopoint_interfaces__srv__MoveToPoint_Response__Sequence
{
  robopoint_interfaces__srv__MoveToPoint_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robopoint_interfaces__srv__MoveToPoint_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOPOINT_INTERFACES__SRV__DETAIL__MOVE_TO_POINT__STRUCT_H_
