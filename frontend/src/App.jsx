import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";

import Login from "./auth/Login";
import Register from "./auth/Register";
import Shop from "./pages/Shop";
import Admin from "./pages/Admin";
import ProtectedRoute from "./auth/ProtectedRoute";

export default function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<Shop />} />
        <Route
          path="/shop"
          element={
            <ProtectedRoute>
              <Shop />
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        

        <Route
          path="/admin"
          element={
            <ProtectedRoute adminOnly>
              <Admin />
            </ProtectedRoute>
          }
        />
      </Routes>
    </>
  );
}
