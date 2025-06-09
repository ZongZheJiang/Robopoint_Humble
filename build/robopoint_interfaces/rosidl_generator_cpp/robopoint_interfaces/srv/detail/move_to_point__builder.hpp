// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robopoint_interfaces:srv/MoveToPoint.idl
// generated code does not contain a copyright notice

#ifndef ROBOPOINT_INTERFACES__SRV__DETAIL__MOVE_TO_POINT__BUILDER_HPP_
#define ROBOPOINT_INTERFACES__SRV__DETAIL__MOVE_TO_POINT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robopoint_interfaces/srv/detail/move_to_point__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robopoint_interfaces
{

namespace srv
{

namespace builder
{

class Init_MoveToPoint_Request_y
{
public:
  explicit Init_MoveToPoint_Request_y(::robopoint_interfaces::srv::MoveToPoint_Request & msg)
  : msg_(msg)
  {}
  ::robopoint_interfaces::srv::MoveToPoint_Request y(::robopoint_interfaces::srv::MoveToPoint_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robopoint_interfaces::srv::MoveToPoint_Request msg_;
};

class Init_MoveToPoint_Request_x
{
public:
  Init_MoveToPoint_Request_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveToPoint_Request_y x(::robopoint_interfaces::srv::MoveToPoint_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_MoveToPoint_Request_y(msg_);
  }

private:
  ::robopoint_interfaces::srv::MoveToPoint_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robopoint_interfaces::srv::MoveToPoint_Request>()
{
  return robopoint_interfaces::srv::builder::Init_MoveToPoint_Request_x();
}

}  // namespace robopoint_interfaces


namespace robopoint_interfaces
{

namespace srv
{

namespace builder
{

class Init_MoveToPoint_Response_success
{
public:
  Init_MoveToPoint_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::robopoint_interfaces::srv::MoveToPoint_Response success(::robopoint_interfaces::srv::MoveToPoint_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robopoint_interfaces::srv::MoveToPoint_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robopoint_interfaces::srv::MoveToPoint_Response>()
{
  return robopoint_interfaces::srv::builder::Init_MoveToPoint_Response_success();
}

}  // namespace robopoint_interfaces

#endif  // ROBOPOINT_INTERFACES__SRV__DETAIL__MOVE_TO_POINT__BUILDER_HPP_
