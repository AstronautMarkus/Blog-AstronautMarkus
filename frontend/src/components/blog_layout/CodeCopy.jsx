import { useEffect } from "react";

export default function CodeCopy() {
    useEffect(() => {
        const pres = document.querySelectorAll('pre.astro-code');
        pres.forEach(pre => {
            if (pre.querySelector('.code-copy-btn')) return;

            const codeElem = pre.querySelector('code');
            if (!codeElem) return;

            const btn = document.createElement('button');
            btn.innerHTML = `<i class="hn hn-copy-solid"></i> <span>Copy</span>`;
            btn.className = "code-copy-btn bg-[#c5c1c0] hover:bg-gray-200 text-gray-700 px-2 py-1 text-sm ml-2 mt-1 flex items-center gap-1 transition";
            btn.style.position = "absolute";
            btn.style.top = "8px";
            btn.style.right = "8px";
            btn.style.zIndex = "10";
            btn.style.borderRadius = "0.25rem";
            btn.style.border = "none";
            btn.style.cursor = "pointer";

            pre.style.position = "relative";

            btn.onclick = async (e) => {
                e.stopPropagation();
                await navigator.clipboard.writeText(codeElem.innerText);
                btn.innerHTML = `<i class="hn hn-thumbsup-solid"></i> <span>Copied!</span>`;
                setTimeout(() => {
                    btn.innerHTML = `<i class="hn hn-copy-solid"></i> <span>Copy</span>`;
                }, 2000);
            };

            pre.appendChild(btn);
        });
    }, []);

    return null;
}
