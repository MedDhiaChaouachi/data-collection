import React from "react";

export const SelectValue = ({ placeholder }) => {
  return (
    <div className="flex justify-between w-full py-2">
      <span className="block text-sm text-gray-700">{placeholder}</span>
      <svg
        className="w-4 h-4 ml-2 text-gray-500"
        viewBox="0 0 20 20"
        fill="currentColor"
      >
        <path
          fillRule="evenodd"
          d="M9.293 12.293a1 1 0 011.414 0l4 4a1 1 0 01-1.414 1.414L10 14.414l-3.293 3.293a1 1 0 01-1.414-1.414l4-4a1 1 0 010-1.414z"
          clipRule="evenodd"
        />
      </svg>
    </div>
  );
};

export const SelectTrigger = ({ className, children }) => {
  return (
    <div
      className={`relative w-full border border-gray-300 rounded-md focus-within:ring-1 focus-within:ring-purple-500 focus-within:border-purple-500 ${className}`}
    >
      {children}
    </div>
  );
};

export const SelectItem = ({ value, children }) => {
  return <option value={value}>{children}</option>;
};

export const SelectContent = ({ children }) => {
  return (
    <select className="absolute z-10 block w-full py-2 mt-1 overflow-auto bg-white rounded-md shadow-lg max-h-60 focus:outline-none sm:text-sm">
      {children}
    </select>
  );
};

export const Select = ({ defaultValue, id, children }) => {
  return (
    <div className="relative">
      <select id={id} defaultValue={defaultValue} className="sr-only">
        {children}
      </select>
    </div>
  );
};
