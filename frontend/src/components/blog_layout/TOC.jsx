import { useEffect, useState } from "react";

export default function TOC() {
    const [headings, setHeadings] = useState([]);
    const [mobileOpen, setMobileOpen] = useState(false);

    useEffect(() => {
        const elements = Array.from(
            document.querySelectorAll(".markdown-content h1, .markdown-content h2, .markdown-content h3")
        );
        const parsed = elements.map((el) => ({
            id: el.id || "",
            text: el.innerText,
            level: Number(el.tagName.replace("H", ""))
        }));
        setHeadings(parsed);
    }, []);

    useEffect(() => {
        if (mobileOpen) {
            document.body.style.overflow = "hidden";
        } else {
            document.body.style.overflow = "";
        }
        return () => {
            document.body.style.overflow = "";
        };
    }, [mobileOpen]);

    return (
        <>
            <ul className="space-y-1 hidden md:block">
                <li>
                    <button
                        onClick={() => window.scrollTo({ top: 0, behavior: "smooth" })}
                        className="hover:underline text-gray-700 font-medium bg-transparent border-none p-0 m-0 cursor-pointer"
                        style={{ background: "none" }}
                    >
                        Index
                    </button>
                </li>
                {headings.map((h, idx) => (
                    <li key={idx} className={`ml-${(h.level - 1) * 2}`}>
                        <a href={`#${h.id}`} className="hover:underline text-gray-700 font-medium">
                            {h.text}
                        </a>
                    </li>
                ))}
            </ul>

            <button
                className="fixed bottom-6 right-6 z-40 md:hidden bg-[#c5c1c0] text-gray-800 rounded-full shadow-lg p-3 flex items-center gap-2 font-semibold focus:outline-none transition hover:bg-[#b1aeae]"
                aria-label="Open Table of Contents"
                onClick={() => setMobileOpen(true)}
                style={{boxShadow: "0 4px 24px 0 rgba(0,0,0,0.10)"}}
            >
                <i className="hn hn-bars-solid"></i>
            </button>

            <div
                className={`fixed inset-0 bg-black/40 z-50 transition-opacity duration-300 ${mobileOpen ? "opacity-100 pointer-events-auto" : "opacity-0 pointer-events-none"} md:hidden`}
                onClick={() => setMobileOpen(false)}
            />

            <aside
                className={`fixed top-0 right-0 h-full w-72 max-w-full bg-[#f7f7f7] z-50 shadow-2xl transform transition-transform duration-300 md:hidden flex flex-col
                ${mobileOpen ? "translate-x-0" : "translate-x-full"}`}
                style={{willChange: "transform"}}
            >
                <div className="flex items-center justify-between px-5 py-4 border-b border-[#ADADAD] bg-[#c5c1c0]">
                    <span className="font-bold mb-2 playstation-fonts text-gray-800 md:text-xl text-center">Table of Contents</span>
                    <button
                        className="text-gray-700 hover:bg-gray-200 rounded-full p-2 transition"
                        aria-label="Close TOC"
                        onClick={() => setMobileOpen(false)}
                    >
                        <i className="hn hn-times-solid"></i>
                    </button>
                </div>
                <nav className="flex-1 overflow-y-auto px-5 py-4 bg-[#ADADAD]">
                    <ul className="space-y-2">
                        <li>
                            <button
                                onClick={() => {
                                    window.scrollTo({ top: 0, behavior: "smooth" });
                                    setMobileOpen(false);
                                }}
                                className="hover:underline text-gray-700 font-medium bg-transparent border-none p-0 m-0 cursor-pointer"
                                style={{ background: "none" }}
                            >
                                Index
                            </button>
                        </li>
                        {headings.length === 0 && (
                            <li className="text-gray-500">No headings found</li>
                        )}
                        {headings.map((h, idx) => (
                            <li key={idx} className={`ml-${(h.level - 1) * 3}`}>
                                <a
                                    href={`#${h.id}`}
                                    className="block py-1 px-2 rounded hover:bg-blue-100 hover:text-blue-700 text-gray-800 font-medium transition"
                                    onClick={() => setMobileOpen(false)}
                                >
                                    {h.text}
                                </a>
                            </li>
                        ))}
                    </ul>
                </nav>
            </aside>
        </>
    );
}
