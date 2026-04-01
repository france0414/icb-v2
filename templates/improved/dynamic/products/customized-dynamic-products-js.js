document.addEventListener("DOMContentLoaded", function () {
    if (document.body.classList.contains("editor_started")) return;
    // 防抖函式，避免頻繁觸發
    function debounce(fn, delay) {
        let timer = null;
        return function (...args) {
            clearTimeout(timer);
            timer = setTimeout(() => fn.apply(this, args), delay);
        };
    }
    // 合併同一容器內多個 .row 的子元素
    function mergeRows(container) {
        const rows = Array.from(container.children).filter(child => child.classList.contains('row'));
        if (rows.length > 1) {
            const firstRow = rows[0];
            for (let i = 1; i < rows.length; i++) {
                const currentRow = rows[i];
                while (currentRow.firstElementChild) {
                    firstRow.appendChild(currentRow.firstElementChild);
                }
                currentRow.remove();
            }
        }
    }
    // 平滑滾動函式（含緩動）
    function smoothScrollBy(container, distance, duration = 300) {
        const start = container.scrollLeft;
        const startTime = performance.now();
        function scrollStep(timestamp) {
            const elapsed = timestamp - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const ease = 0.5 - Math.cos(progress * Math.PI) / 2;
            container.scrollLeft = start + distance * ease;
            if (progress < 1) {
                requestAnimationFrame(scrollStep);
            }
        }
        requestAnimationFrame(scrollStep);
    }
    let isScrollingLocked = false;
    const scrollCooldown = 800;
    // 初始化每個 row 元素的滾動與箭頭行為
    function initRowElements() {
        const rowElements = document.querySelectorAll(".s_custom_productRightScroll >[class*=container]>[class*=_snippet_template]>.row");
        rowElements.forEach((rowElement) => {
            rowElement.style.overflowX = "auto";
            rowElement.style.overflowY = "hidden";
            rowElement.style.overscrollBehaviorX = "contain";
            // 檢查箭頭是否已存在，若無才新增
            let leftArrow = rowElement.parentElement.querySelector('.carousel-arrow-left');
            let rightArrow = rowElement.parentElement.querySelector('.carousel-arrow-right');
            if (!leftArrow) {
                leftArrow = document.createElement("div");
                leftArrow.classList.add("carousel-arrow", "carousel-arrow-left");
                leftArrow.innerHTML = '<i class="fa fa-angle-left" aria-hidden="true"></i>';
                rowElement.parentElement.appendChild(leftArrow);
            }
            if (!rightArrow) {
                rightArrow = document.createElement("div");
                rightArrow.classList.add("carousel-arrow", "carousel-arrow-right");
                rightArrow.innerHTML = '<i class="fa fa-angle-right" aria-hidden="true"></i>';
                rowElement.parentElement.appendChild(rightArrow);
            }
            // 如果沒有橫向卷軸，就隱藏箭頭
            const isScrollable = rowElement.scrollWidth > rowElement.clientWidth;
            leftArrow.style.display = isScrollable ? 'block' : 'none';
            rightArrow.style.display = isScrollable ? 'block' : 'none';
            // 滾動事件控制箭頭啟用狀態
            rowElement.addEventListener("scroll", function () {
                const maxScrollLeft = rowElement.scrollWidth - rowElement.clientWidth;
                const currentScrollLeft = rowElement.scrollLeft;
                leftArrow.classList.toggle("disabled", currentScrollLeft <= 0);
                rightArrow.classList.toggle("disabled", currentScrollLeft >= maxScrollLeft);
            });
            // 滑鼠滾輪滾動（含上下頁切換）
            rowElement.addEventListener(
                "wheel",
                function (e) {
                    const maxScrollLeft = rowElement.scrollWidth - rowElement.clientWidth;
                    const currentScrollLeft = rowElement.scrollLeft;
                    const atLeftEdge = currentScrollLeft <= 0;
                    const atRightEdge = currentScrollLeft >= maxScrollLeft;
                    if ((atLeftEdge && e.deltaY < 0) || (atRightEdge && e.deltaY > 0)) {
                        if (isScrollingLocked) return;
                        e.preventDefault();
                        isScrollingLocked = true;
                        setTimeout(() => {
                            isScrollingLocked = false;
                        }, scrollCooldown);
                    } else {
                        e.preventDefault();
                        smoothScrollBy(rowElement, e.deltaY * 2, 400);
                    }
                },
                { passive: false }
            );
            // 左箭頭點擊事件
            leftArrow.addEventListener("click", function () {
                const scrollDistance = getComputedStyle(document.documentElement).getPropertyValue('--scroll-distance');
                const distance = parseFloat(scrollDistance) * window.innerWidth / 100;
                smoothScrollBy(rowElement, -distance);
            });
            // 右箭頭點擊事件
            rightArrow.addEventListener("click", function () {
                const scrollDistance = getComputedStyle(document.documentElement).getPropertyValue('--scroll-distance');
                const distance = parseFloat(scrollDistance) * window.innerWidth / 100;
                smoothScrollBy(rowElement, distance);
            });
        });
    }
    // 主流程：合併 row 並初始化
    function processContainers() {
        const containers = document.querySelectorAll('.s_custom_productRightScroll >[class*=container]>[class*=_snippet_template]');
        containers.forEach(container => {
            mergeRows(container);
        });
        initRowElements();
    }
    // 監聽 .dynamic_snippet_template 內部新增元素
    function startObserver() {
        const targets = document.querySelectorAll('.s_custom_productRightScroll >[class*=container]>[class*=_snippet_template]');
        if (targets.length === 0) {
            setTimeout(startObserver, 300); // 等待動態生成
            return;
        }
        const debouncedProcess = debounce(processContainers, 200);
        const observer = new MutationObserver((mutationsList) => {
            for (const mutation of mutationsList) {
                if (mutation.type === 'childList' && mutation.addedNodes.length > 0) {
                    debouncedProcess();
                    break;
                }
            }
        });
        targets.forEach(target => {
            observer.observe(target, { childList: true, subtree: false });
        });
    }
    // 頁面載入時先執行一次初始化
    processContainers();
    // 啟動監聽器
    startObserver();
});
