// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robopoint_interfaces:srv/MoveToPoint.idl
// generated code does not contain a copyright notice

#ifndef ROBOPOINT_INTERFACES__SRV__DETAIL__MOVE_TO_POINT__STRUCT_HPP_
#define ROBOPOINT_INTERFACES__SRV__DETAIL__MOVE_TO_POINT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__robopoint_interfaces__srv__MoveToPoint_Request __attribute__((deprecated))
#else
# define DEPRECATED__robopoint_interfaces__srv__MoveToPoint_Request __declspec(deprecated)
#endif

namespace robopoint_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MoveToPoint_Request_
{
  using Type = MoveToPoint_Request_<ContainerAllocator>;

  explicit MoveToPoint_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0.0f;
      this->y = 0.0f;
      this->z = 0.0f;
    }
  }

  explicit MoveToPoint_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->x = 0.0f;
      this->y = 0.0f;
      this->z = 0.0f;
    }
  }

  // field types and members
  using _x_type =
    float;
  _x_type x;
  using _y_type =
    float;
  _y_type y;
  using _z_type =
    float;
  _z_type z;

  // setters for named parameter idiom
  Type & set__x(
    const float & _arg)
  {
    this->x = _arg;
    return *this;
  }
  Type & set__y(
    const float & _arg)
  {
    this->y = _arg;
    return *this;
  }
  Type & set__z(
    const float & _arg)
  {
    this->z = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robopoint_interfaces__srv__MoveToPoint_Request
    std::shared_ptr<robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robopoint_interfaces__srv__MoveToPoint_Request
    std::shared_ptr<robopoint_interfaces::srv::MoveToPoint_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveToPoint_Request_ & other) const
  {
    if (this->x != other.x) {
      return false;
    }
    if (this->y != other.y) {
      return false;
    }
    if (this->z != other.z) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveToPoint_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveToPoint_Request_

// alias to use template instance with default allocator
using MoveToPoint_Request =
  robopoint_interfaces::srv::MoveToPoint_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robopoint_interfaces


#ifndef _WIN32
# define DEPRECATED__robopoint_interfaces__srv__MoveToPoint_Response __attribute__((deprecated))
#else
# define DEPRECATED__robopoint_interfaces__srv__MoveToPoint_Response __declspec(deprecated)
#endif

namespace robopoint_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct MoveToPoint_Response_
{
  using Type = MoveToPoint_Response_<ContainerAllocator>;

  explicit MoveToPoint_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit MoveToPoint_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations

  // pointer types
  using RawPtr =
    robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robopoint_interfaces__srv__MoveToPoint_Response
    std::shared_ptr<robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robopoint_interfaces__srv__MoveToPoint_Response
    std::shared_ptr<robopoint_interfaces::srv::MoveToPoint_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveToPoint_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveToPoint_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveToPoint_Response_

// alias to use template instance with default allocator
using MoveToPoint_Response =
  robopoint_interfaces::srv::MoveToPoint_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robopoint_interfaces

namespace robopoint_interfaces
{

namespace srv
{

struct MoveToPoint
{
  using Request = robopoint_interfaces::srv::MoveToPoint_Request;
  using Response = robopoint_interfaces::srv::MoveToPoint_Response;
};

}  // namespace srv

}  // namespace robopoint_interfaces

#endif  // ROBOPOINT_INTERFACES__SRV__DETAIL__MOVE_TO_POINT__STRUCT_HPP_
