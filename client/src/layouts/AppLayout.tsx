import { Outlet } from "react-router-dom";
import Header from "../components/Header";
import Footer from "../components/Footer";

function AppLayout() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header />

      <main className="flex-1 w-full max-w-3xl mx-auto px-4 py-8">
        <Outlet />
      </main>

      <Footer />
    </div>
  );
}

export default AppLayout;
