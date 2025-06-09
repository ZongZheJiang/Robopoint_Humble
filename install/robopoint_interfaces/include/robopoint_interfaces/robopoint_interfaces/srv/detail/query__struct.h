// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from robopoint_interfaces:srv/Query.idl
// generated code does not contain a copyright notice

#ifndef ROBOPOINT_INTERFACES__SRV__DETAIL__QUERY__STRUCT_H_
#define ROBOPOINT_INTERFACES__SRV__DETAIL__QUERY__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'query'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/Query in the package robopoint_interfaces.
typedef struct robopoint_interfaces__srv__Query_Request
{
  rosidl_runtime_c__String query;
} robopoint_interfaces__srv__Query_Request;

// Struct for a sequence of robopoint_interfaces__srv__Query_Request.
typedef struct robopoint_interfaces__srv__Query_Request__Sequence
{
  robopoint_interfaces__srv__Query_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robopoint_interfaces__srv__Query_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/Query in the package robopoint_interfaces.
typedef struct robopoint_interfaces__srv__Query_Response
{
  uint8_t structure_needs_at_least_one_member;
} robopoint_interfaces__srv__Query_Response;

// Struct for a sequence of robopoint_interfaces__srv__Query_Response.
typedef struct robopoint_interfaces__srv__Query_Response__Sequence
{
  robopoint_interfaces__srv__Query_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} robopoint_interfaces__srv__Query_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // ROBOPOINT_INTERFACES__SRV__DETAIL__QUERY__STRUCT_H_
