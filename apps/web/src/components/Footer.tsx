export default function Footer() {
  return (
    <footer className="bg-gray-800 text-gray-200 text-center py-4 mt-10">
      <p>© {new Date().getFullYear()} Open Recipe Hub. Built with ❤️ for Hacktoberfest.</p>
    </footer>
  );
}
