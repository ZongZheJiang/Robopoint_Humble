// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from robopoint_interfaces:srv/Get3DCoordinates.idl
// generated code does not contain a copyright notice

#ifndef ROBOPOINT_INTERFACES__SRV__DETAIL__GET3_D_COORDINATES__FUNCTIONS_H_
#define ROBOPOINT_INTERFACES__SRV__DETAIL__GET3_D_COORDINATES__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "robopoint_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "robopoint_interfaces/srv/detail/get3_d_coordinates__struct.h"

/// Initialize srv/Get3DCoordinates message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * robopoint_interfaces__srv__Get3DCoordinates_Request
 * )) before or use
 * robopoint_interfaces__srv__Get3DCoordinates_Request__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Request__init(robopoint_interfaces__srv__Get3DCoordinates_Request * msg);

/// Finalize srv/Get3DCoordinates message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
void
robopoint_interfaces__srv__Get3DCoordinates_Request__fini(robopoint_interfaces__srv__Get3DCoordinates_Request * msg);

/// Create srv/Get3DCoordinates message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * robopoint_interfaces__srv__Get3DCoordinates_Request__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
robopoint_interfaces__srv__Get3DCoordinates_Request *
robopoint_interfaces__srv__Get3DCoordinates_Request__create();

/// Destroy srv/Get3DCoordinates message.
/**
 * It calls
 * robopoint_interfaces__srv__Get3DCoordinates_Request__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
void
robopoint_interfaces__srv__Get3DCoordinates_Request__destroy(robopoint_interfaces__srv__Get3DCoordinates_Request * msg);

/// Check for srv/Get3DCoordinates message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Request__are_equal(const robopoint_interfaces__srv__Get3DCoordinates_Request * lhs, const robopoint_interfaces__srv__Get3DCoordinates_Request * rhs);

/// Copy a srv/Get3DCoordinates message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Request__copy(
  const robopoint_interfaces__srv__Get3DCoordinates_Request * input,
  robopoint_interfaces__srv__Get3DCoordinates_Request * output);

/// Initialize array of srv/Get3DCoordinates messages.
/**
 * It allocates the memory for the number of elements and calls
 * robopoint_interfaces__srv__Get3DCoordinates_Request__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence__init(robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence * array, size_t size);

/// Finalize array of srv/Get3DCoordinates messages.
/**
 * It calls
 * robopoint_interfaces__srv__Get3DCoordinates_Request__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
void
robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence__fini(robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence * array);

/// Create array of srv/Get3DCoordinates messages.
/**
 * It allocates the memory for the array and calls
 * robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence *
robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence__create(size_t size);

/// Destroy array of srv/Get3DCoordinates messages.
/**
 * It calls
 * robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
void
robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence__destroy(robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence * array);

/// Check for srv/Get3DCoordinates message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence__are_equal(const robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence * lhs, const robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence * rhs);

/// Copy an array of srv/Get3DCoordinates messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence__copy(
  const robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence * input,
  robopoint_interfaces__srv__Get3DCoordinates_Request__Sequence * output);

/// Initialize srv/Get3DCoordinates message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * robopoint_interfaces__srv__Get3DCoordinates_Response
 * )) before or use
 * robopoint_interfaces__srv__Get3DCoordinates_Response__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Response__init(robopoint_interfaces__srv__Get3DCoordinates_Response * msg);

/// Finalize srv/Get3DCoordinates message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
void
robopoint_interfaces__srv__Get3DCoordinates_Response__fini(robopoint_interfaces__srv__Get3DCoordinates_Response * msg);

/// Create srv/Get3DCoordinates message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * robopoint_interfaces__srv__Get3DCoordinates_Response__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
robopoint_interfaces__srv__Get3DCoordinates_Response *
robopoint_interfaces__srv__Get3DCoordinates_Response__create();

/// Destroy srv/Get3DCoordinates message.
/**
 * It calls
 * robopoint_interfaces__srv__Get3DCoordinates_Response__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
void
robopoint_interfaces__srv__Get3DCoordinates_Response__destroy(robopoint_interfaces__srv__Get3DCoordinates_Response * msg);

/// Check for srv/Get3DCoordinates message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Response__are_equal(const robopoint_interfaces__srv__Get3DCoordinates_Response * lhs, const robopoint_interfaces__srv__Get3DCoordinates_Response * rhs);

/// Copy a srv/Get3DCoordinates message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Response__copy(
  const robopoint_interfaces__srv__Get3DCoordinates_Response * input,
  robopoint_interfaces__srv__Get3DCoordinates_Response * output);

/// Initialize array of srv/Get3DCoordinates messages.
/**
 * It allocates the memory for the number of elements and calls
 * robopoint_interfaces__srv__Get3DCoordinates_Response__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence__init(robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence * array, size_t size);

/// Finalize array of srv/Get3DCoordinates messages.
/**
 * It calls
 * robopoint_interfaces__srv__Get3DCoordinates_Response__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
void
robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence__fini(robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence * array);

/// Create array of srv/Get3DCoordinates messages.
/**
 * It allocates the memory for the array and calls
 * robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence *
robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence__create(size_t size);

/// Destroy array of srv/Get3DCoordinates messages.
/**
 * It calls
 * robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
void
robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence__destroy(robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence * array);

/// Check for srv/Get3DCoordinates message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence__are_equal(const robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence * lhs, const robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence * rhs);

/// Copy an array of srv/Get3DCoordinates messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_robopoint_interfaces
bool
robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence__copy(
  const robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence * input,
  robopoint_interfaces__srv__Get3DCoordinates_Response__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // ROBOPOINT_INTERFACES__SRV__DETAIL__GET3_D_COORDINATES__FUNCTIONS_H_
