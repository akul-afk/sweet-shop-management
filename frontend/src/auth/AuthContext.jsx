import { createContext, useContext, useState } from "react";
import api from "../api/axios";

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(() => localStorage.getItem("token"));
  const [role, setRole] = useState(() => localStorage.getItem("role")); // user/admin

  const login = async (email, password, roleType = "user") => {
    const res = await api.post("/api/auth/login", {
      email,
      password,
      role: roleType,
    });

    localStorage.setItem("token", res.data.access_token);
    localStorage.setItem("role", roleType);

    setToken(res.data.access_token);
    setRole(roleType);
  };

  const register = async (email, password, roleType = "user") => {
    await api.post("/api/auth/register", {
      email,
      password,
      role: roleType,
    });
  };

  const logout = () => {
    localStorage.clear();
    setToken(null);
    setRole(null);
  };

  return (
    <AuthContext.Provider
      value={{
        token,
        role,
        isAuthenticated: !!token,
        login,
        register,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
