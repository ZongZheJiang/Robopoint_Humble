// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from robopoint_interfaces:srv/Get3DCoordinates.idl
// generated code does not contain a copyright notice

#ifndef ROBOPOINT_INTERFACES__SRV__DETAIL__GET3_D_COORDINATES__BUILDER_HPP_
#define ROBOPOINT_INTERFACES__SRV__DETAIL__GET3_D_COORDINATES__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "robopoint_interfaces/srv/detail/get3_d_coordinates__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace robopoint_interfaces
{

namespace srv
{

namespace builder
{

class Init_Get3DCoordinates_Request_y
{
public:
  explicit Init_Get3DCoordinates_Request_y(::robopoint_interfaces::srv::Get3DCoordinates_Request & msg)
  : msg_(msg)
  {}
  ::robopoint_interfaces::srv::Get3DCoordinates_Request y(::robopoint_interfaces::srv::Get3DCoordinates_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robopoint_interfaces::srv::Get3DCoordinates_Request msg_;
};

class Init_Get3DCoordinates_Request_x
{
public:
  Init_Get3DCoordinates_Request_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Get3DCoordinates_Request_y x(::robopoint_interfaces::srv::Get3DCoordinates_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Get3DCoordinates_Request_y(msg_);
  }

private:
  ::robopoint_interfaces::srv::Get3DCoordinates_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robopoint_interfaces::srv::Get3DCoordinates_Request>()
{
  return robopoint_interfaces::srv::builder::Init_Get3DCoordinates_Request_x();
}

}  // namespace robopoint_interfaces


namespace robopoint_interfaces
{

namespace srv
{

namespace builder
{

class Init_Get3DCoordinates_Response_z
{
public:
  explicit Init_Get3DCoordinates_Response_z(::robopoint_interfaces::srv::Get3DCoordinates_Response & msg)
  : msg_(msg)
  {}
  ::robopoint_interfaces::srv::Get3DCoordinates_Response z(::robopoint_interfaces::srv::Get3DCoordinates_Response::_z_type arg)
  {
    msg_.z = std::move(arg);
    return std::move(msg_);
  }

private:
  ::robopoint_interfaces::srv::Get3DCoordinates_Response msg_;
};

class Init_Get3DCoordinates_Response_y
{
public:
  explicit Init_Get3DCoordinates_Response_y(::robopoint_interfaces::srv::Get3DCoordinates_Response & msg)
  : msg_(msg)
  {}
  Init_Get3DCoordinates_Response_z y(::robopoint_interfaces::srv::Get3DCoordinates_Response::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Get3DCoordinates_Response_z(msg_);
  }

private:
  ::robopoint_interfaces::srv::Get3DCoordinates_Response msg_;
};

class Init_Get3DCoordinates_Response_x
{
public:
  Init_Get3DCoordinates_Response_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Get3DCoordinates_Response_y x(::robopoint_interfaces::srv::Get3DCoordinates_Response::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Get3DCoordinates_Response_y(msg_);
  }

private:
  ::robopoint_interfaces::srv::Get3DCoordinates_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::robopoint_interfaces::srv::Get3DCoordinates_Response>()
{
  return robopoint_interfaces::srv::builder::Init_Get3DCoordinates_Response_x();
}

}  // namespace robopoint_interfaces

#endif  // ROBOPOINT_INTERFACES__SRV__DETAIL__GET3_D_COORDINATES__BUILDER_HPP_
