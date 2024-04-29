import React from "react";

const Button = ({ className, children, ...rest }) => {
  return (
    <button
      className={`inline-flex items-center justify-center px-4 py-2 text-sm font-medium text-white bg-purple-600 border border-transparent rounded-md hover:bg-purple-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-purple-500 ${className}`}
      {...rest}
    >
      {children}
    </button>
  );
};

export default Button;
