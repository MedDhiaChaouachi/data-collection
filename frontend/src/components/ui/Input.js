import React from "react";

const Input = ({ id, type, placeholder, required }) => {
  return (
    <input
      id={id}
      type={type}
      placeholder={placeholder}
      required={required}
      className="block w-full px-3 py-2 mt-1 text-sm border-gray-300 rounded-md focus:outline-none focus:ring-indigo-500 focus:border-indigo-500"
    />
  );
};

export default Input;
