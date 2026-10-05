document.addEventListener("DOMContentLoaded", () => {
    const blocks = Array.from(document.querySelectorAll(".textselect-block"));
    if (!blocks.length) return;

    blocks.forEach((block) => {
        const isMulti = block.dataset.mode === "multi";
        const shouldShuffle = block.dataset.shuffle === "true";
        const content = block.querySelector(".textselect-content");

        if (!content) return;

        let targetMap = {};
        try {
            targetMap = JSON.parse(content.dataset.targets || "{}");
        } catch (e) {
            console.error("TextSelect: invalid target JSON", e);
        }

        /* ---------------------------------------------------------
           Shuffle lines
        --------------------------------------------------------- */
        function shuffleLines() {
            if (!shouldShuffle) return;

            const lines = Array.from(content.querySelectorAll(".ts-line"));

            for (let i = lines.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));

                const temp = lines[i];
                lines[i] = lines[j];
                lines[j] = temp;
            }

            lines.forEach((line) => content.appendChild(line));
        }

        shuffleLines();

        const words = Array.from(block.querySelectorAll(".ts-word"));

        /* ---------------------------------------------------------
           Determine colours actually used by targets
        --------------------------------------------------------- */
        const activeColorsSet = new Set();

        Object.values(targetMap).forEach((value) => {
            if (Array.isArray(value)) {
                value.forEach((color) =>
                    activeColorsSet.add(String(color).toLowerCase())
                );
            } else if (value) {
                activeColorsSet.add(String(value).toLowerCase());
            }
        });

        const activeColors = Array.from(activeColorsSet);

        /* ---------------------------------------------------------
           Determine single-mode default color:
           1. Check explicit block class (e.g., .ts-color-p)
           2. Fall back to the target color defined in targets JSON
           3. Default to "blue" if neither is present
        --------------------------------------------------------- */
        const colorClass = Array.from(block.classList).find((c) =>
            c.startsWith("ts-color-")
        );

        const singleDefaultColor = colorClass
            ? colorClass.replace("ts-color-", "").toLowerCase()
            : activeColors[0] || "blue";

        let currentColor = isMulti
            ? activeColors[0] || singleDefaultColor
            : singleDefaultColor;

        let isMouseDown = false;
        let lastClickedIdx = null;

        /* ---------------------------------------------------------
           Prevent normal text selection while dragging
        --------------------------------------------------------- */
        content.addEventListener("selectstart", (e) => {
            if (isMouseDown) e.preventDefault();
        });

        /* ---------------------------------------------------------
           Multi-mode palette
        --------------------------------------------------------- */
        if (isMulti && activeColors.length) {
            const palette = document.createElement("div");
            palette.className = "textselect-palette";

            const paletteButtons = {};

            activeColors.forEach((color) => {
                const button = document.createElement("button");

                button.type = "button";
                button.className = `ts-palette-btn ts-color-${color}`;
                button.textContent = color.toUpperCase();

                if (color === currentColor) {
                    button.classList.add("active");
                }

                button.addEventListener("click", () => {
                    currentColor = color;

                    Object.values(paletteButtons).forEach((btn) => {
                        btn.classList.remove("active");
                    });

                    button.classList.add("active");
                });

                paletteButtons[color] = button;
                palette.appendChild(button);
            });

            block.insertBefore(palette, content);
        }

        /* ---------------------------------------------------------
           Selection helpers
        --------------------------------------------------------- */
        function clearSelectionClasses(word) {
            Array.from(word.classList).forEach((cls) => {
                if (cls.startsWith("ts-sel-")) {
                    word.classList.remove(cls);
                }
            });

            word.classList.remove("selected");
            delete word.dataset.selectedColor;
        }

        function setWordColor(word, color, toggle = true) {
            if (isMulti) {
                const existing = word.dataset.selectedColor;

                if (toggle && existing === color) {
                    clearSelectionClasses(word);
                    return;
                }

                clearSelectionClasses(word);

                word.dataset.selectedColor = color;
                word.classList.add("selected", `ts-sel-${color}`);
            } else {
                if (toggle && word.classList.contains("selected")) {
                    clearSelectionClasses(word);
                    return;
                }

                clearSelectionClasses(word);

                word.dataset.selectedColor = singleDefaultColor;
                word.classList.add(
                    "selected",
                    `ts-sel-${singleDefaultColor}`
                );
            }
        }

        /* ---------------------------------------------------------
           Interactive word selection
        --------------------------------------------------------- */
        words.forEach((word) => {
            const idx = parseInt(word.dataset.idx, 10);

            word.addEventListener("mousedown", (e) => {
                if (block.dataset.disabled === "true") return;

                e.preventDefault();
                isMouseDown = true;

                if (e.shiftKey && lastClickedIdx !== null) {
                    const start = Math.min(lastClickedIdx, idx);
                    const end = Math.max(lastClickedIdx, idx);

                    for (let i = start; i <= end; i++) {
                        if (words[i]) {
                            setWordColor(words[i], currentColor, false);
                        }
                    }
                } else {
                    setWordColor(word, currentColor, true);
                    lastClickedIdx = idx;
                }
            });

            word.addEventListener("mouseenter", () => {
                if (
                    isMouseDown &&
                    block.dataset.disabled !== "true"
                ) {
                    setWordColor(word, currentColor, false);
                }
            });
        });

        window.addEventListener("mouseup", () => {
            isMouseDown = false;
        });

        /* ---------------------------------------------------------
           Control panel
        --------------------------------------------------------- */
        const panel = document.createElement("div");
        panel.className = "textselect-global-panel";

        const btnScore = document.createElement("button");
        btnScore.type = "button";
        btnScore.className = "textselect-btn-score";
        btnScore.textContent = "Check";

        const btnReset = document.createElement("button");
        btnReset.type = "button";
        btnReset.className = "textselect-btn-reset";
        btnReset.textContent = "Reset";

        const scoreBadge = document.createElement("span");
        scoreBadge.className = "textselect-output";
        scoreBadge.style.display = "none";

        panel.appendChild(btnScore);
        panel.appendChild(btnReset);
        panel.appendChild(scoreBadge);

        block.appendChild(panel);

        /* ---------------------------------------------------------
           Group consecutive scored tokens into phrases
        --------------------------------------------------------- */
        function groupTokensInContainer(
            container,
            tokenClass,
            wrapperBaseClass
        ) {
            const nodes = Array.from(container.childNodes);

            let currentGroup = [];
            let currentGroupColor = null;

            function finalizeGroup() {
                if (!currentGroup.length) return;

                while (
                    currentGroup.length &&
                    currentGroup[currentGroup.length - 1].nodeType === 1 &&
                    currentGroup[currentGroup.length - 1].classList.contains(
                        "ts-space"
                    )
                ) {
                    currentGroup.pop();
                }

                if (!currentGroup.length) {
                    currentGroup = [];
                    currentGroupColor = null;
                    return;
                }

                const wrapper = document.createElement("span");

                const appliedColor =
                    currentGroupColor ||
                    `ts-keep-${singleDefaultColor}`;

                wrapper.className =
                    `${wrapperBaseClass} ${appliedColor}`.trim();

                const firstNode = currentGroup[0];

                firstNode.parentNode.insertBefore(wrapper, firstNode);

                currentGroup.forEach((node) => {
                    wrapper.appendChild(node);
                });

                currentGroup = [];
                currentGroupColor = null;
            }

            nodes.forEach((node, i) => {
                const isTargetToken =
                    node.nodeType === 1 &&
                    node.classList.contains(tokenClass);

                let tokenColor = null;

                if (isTargetToken) {
                    tokenColor =
                        Array.from(node.classList).find((cls) =>
                            cls.startsWith("ts-keep-")
                        ) ||
                        `ts-keep-${singleDefaultColor}`;
                }

                let isInternalSpace = false;

                if (
                    node.nodeType === 1 &&
                    node.classList.contains("ts-space") &&
                    currentGroup.length
                ) {
                    const nextNode = nodes[i + 1];

                    if (
                        nextNode &&
                        nextNode.nodeType === 1 &&
                        nextNode.classList.contains(tokenClass)
                    ) {
                        const nextColor =
                            Array.from(nextNode.classList).find((cls) =>
                                cls.startsWith("ts-keep-")
                            ) ||
                            `ts-keep-${singleDefaultColor}`;

                        if (
                            !isMulti ||
                            nextColor === currentGroupColor
                        ) {
                            isInternalSpace = true;
                        }
                    }
                }

                if (
                    isTargetToken &&
                    (
                        !currentGroupColor ||
                        !isMulti ||
                        currentGroupColor === tokenColor
                    )
                ) {
                    currentGroupColor = tokenColor;
                    currentGroup.push(node);
                } else if (isInternalSpace) {
                    currentGroup.push(node);
                } else {
                    finalizeGroup();

                    if (isTargetToken) {
                        currentGroupColor = tokenColor;
                        currentGroup.push(node);
                    }
                }
            });

            finalizeGroup();
        }

        /* ---------------------------------------------------------
           Check
        --------------------------------------------------------- */
        btnScore.addEventListener("click", () => {
            block.dataset.disabled = "true";
            btnScore.disabled = true;

            let correctCount = 0;
            let falsePositives = 0;

            const totalTargets = Object.keys(targetMap).length;

            words.forEach((word) => {
                const idx = word.dataset.idx;

                const selectedColor = word.dataset.selectedColor
                    ? word.dataset.selectedColor.toLowerCase()
                    : null;

                const rawTarget = targetMap[idx];

                const targetColors = Array.isArray(rawTarget)
                    ? rawTarget.map((c) => String(c).toLowerCase())
                    : rawTarget
                        ? [String(rawTarget).toLowerCase()]
                        : [];

                word.classList.remove("selected");

                Array.from(word.classList).forEach((cls) => {
                    if (cls.startsWith("ts-sel-")) {
                        word.classList.remove(cls);
                    }
                });

                if (
                    selectedColor &&
                    targetColors.includes(selectedColor)
                ) {
                    word.classList.add(
                        "ts-correct-token",
                        `ts-keep-${selectedColor}`
                    );

                    correctCount++;
                } else if (selectedColor) {
                    word.classList.add("ts-incorrect-token");
                    falsePositives++;
                } else if (targetColors.length) {
                    word.classList.add(
                        "ts-missed-token",
                        `ts-keep-${targetColors[0]}`
                    );
                }
            });

            const lines = Array.from(
                content.querySelectorAll(".ts-line")
            );

            const containers = lines.length ? lines : [content];

            containers.forEach((container) => {
                groupTokensInContainer(
                    container,
                    "ts-correct-token",
                    "ts-correct-phrase"
                );

                groupTokensInContainer(
                    container,
                    "ts-incorrect-token",
                    "ts-incorrect-phrase"
                );

                groupTokensInContainer(
                    container,
                    "ts-missed-token",
                    "ts-missed-phrase"
                );
            });

            scoreBadge.textContent =
                `Found: ${correctCount} / ${totalTargets}` +
                ` (Extra/Wrong: ${falsePositives})`;

            scoreBadge.style.display = "inline-block";

            scoreBadge.className = "textselect-output";

            const accuracy =
                totalTargets === 0
                    ? 0
                    : correctCount / totalTargets;

            if (accuracy >= 0.8 && falsePositives === 0) {
                scoreBadge.classList.add("high");
            } else if (accuracy >= 0.5) {
                scoreBadge.classList.add("medium");
            } else {
                scoreBadge.classList.add("low");
            }
        });

        /* ---------------------------------------------------------
           Reset
        --------------------------------------------------------- */
        btnReset.addEventListener("click", () => {
            block.dataset.disabled = "false";
            btnScore.disabled = false;

            const wrappers = Array.from(
                block.querySelectorAll(
                    ".ts-correct-phrase, " +
                    ".ts-incorrect-phrase, " +
                    ".ts-missed-phrase"
                )
            );

            wrappers.forEach((wrapper) => {
                while (wrapper.firstChild) {
                    wrapper.parentNode.insertBefore(
                        wrapper.firstChild,
                        wrapper
                    );
                }

                wrapper.remove();
            });

            words.forEach((word) => {
                word.className = "ts-word";
                delete word.dataset.selectedColor;
            });

            scoreBadge.style.display = "none";
            scoreBadge.className = "textselect-output";

            lastClickedIdx = null;
            isMouseDown = false;

            shuffleLines();
        });
    });
});