// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from robopoint_interfaces:srv/Query.idl
// generated code does not contain a copyright notice

#ifndef ROBOPOINT_INTERFACES__SRV__DETAIL__QUERY__STRUCT_HPP_
#define ROBOPOINT_INTERFACES__SRV__DETAIL__QUERY__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__robopoint_interfaces__srv__Query_Request __attribute__((deprecated))
#else
# define DEPRECATED__robopoint_interfaces__srv__Query_Request __declspec(deprecated)
#endif

namespace robopoint_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Query_Request_
{
  using Type = Query_Request_<ContainerAllocator>;

  explicit Query_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->query = "";
    }
  }

  explicit Query_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : query(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->query = "";
    }
  }

  // field types and members
  using _query_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _query_type query;

  // setters for named parameter idiom
  Type & set__query(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->query = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    robopoint_interfaces::srv::Query_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const robopoint_interfaces::srv::Query_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robopoint_interfaces::srv::Query_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robopoint_interfaces::srv::Query_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robopoint_interfaces::srv::Query_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robopoint_interfaces::srv::Query_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robopoint_interfaces::srv::Query_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robopoint_interfaces::srv::Query_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robopoint_interfaces::srv::Query_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robopoint_interfaces::srv::Query_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robopoint_interfaces__srv__Query_Request
    std::shared_ptr<robopoint_interfaces::srv::Query_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robopoint_interfaces__srv__Query_Request
    std::shared_ptr<robopoint_interfaces::srv::Query_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Query_Request_ & other) const
  {
    if (this->query != other.query) {
      return false;
    }
    return true;
  }
  bool operator!=(const Query_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Query_Request_

// alias to use template instance with default allocator
using Query_Request =
  robopoint_interfaces::srv::Query_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robopoint_interfaces


#ifndef _WIN32
# define DEPRECATED__robopoint_interfaces__srv__Query_Response __attribute__((deprecated))
#else
# define DEPRECATED__robopoint_interfaces__srv__Query_Response __declspec(deprecated)
#endif

namespace robopoint_interfaces
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct Query_Response_
{
  using Type = Query_Response_<ContainerAllocator>;

  explicit Query_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit Query_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    robopoint_interfaces::srv::Query_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const robopoint_interfaces::srv::Query_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<robopoint_interfaces::srv::Query_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<robopoint_interfaces::srv::Query_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      robopoint_interfaces::srv::Query_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<robopoint_interfaces::srv::Query_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      robopoint_interfaces::srv::Query_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<robopoint_interfaces::srv::Query_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<robopoint_interfaces::srv::Query_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<robopoint_interfaces::srv::Query_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__robopoint_interfaces__srv__Query_Response
    std::shared_ptr<robopoint_interfaces::srv::Query_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__robopoint_interfaces__srv__Query_Response
    std::shared_ptr<robopoint_interfaces::srv::Query_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Query_Response_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const Query_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Query_Response_

// alias to use template instance with default allocator
using Query_Response =
  robopoint_interfaces::srv::Query_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace robopoint_interfaces

namespace robopoint_interfaces
{

namespace srv
{

struct Query
{
  using Request = robopoint_interfaces::srv::Query_Request;
  using Response = robopoint_interfaces::srv::Query_Response;
};

}  // namespace srv

}  // namespace robopoint_interfaces

#endif  // ROBOPOINT_INTERFACES__SRV__DETAIL__QUERY__STRUCT_HPP_
