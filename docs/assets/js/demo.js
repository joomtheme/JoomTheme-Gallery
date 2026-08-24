(() => {
    const menuButton = document.querySelector('.menu-toggle');
    const menu = document.querySelector('.primary-nav');
    const dialog = document.querySelector('.image-dialog');
    const dialogImage = dialog?.querySelector('img');
    const dialogCaption = dialog?.querySelector('#dialog-caption');
    const closeButton = dialog?.querySelector('.dialog-close');
    let opener = null;

    const closeMenu = () => {
        menu?.classList.remove('is-open');
        menuButton?.setAttribute('aria-expanded', 'false');
    };

    menuButton?.addEventListener('click', () => {
        const isOpen = menu?.classList.toggle('is-open');
        menuButton.setAttribute('aria-expanded', String(Boolean(isOpen)));
    });

    menu?.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));

    document.addEventListener('click', (event) => {
        if (menu?.classList.contains('is-open') && !menu.contains(event.target) && !menuButton?.contains(event.target)) {
            closeMenu();
        }
    });

    document.querySelectorAll('[data-image]').forEach((button) => {
        button.addEventListener('click', () => {
            if (!dialog || !dialogImage || !dialogCaption) {
                return;
            }

            opener = button;
            dialogImage.src = button.dataset.image;
            dialogImage.alt = button.querySelector('img')?.alt ?? 'JoomTheme Gallery screenshot';
            dialogCaption.textContent = button.dataset.caption ?? '';
            document.body.classList.add('dialog-open');
            dialog.showModal();
        });
    });

    const closeDialog = () => dialog?.close();

    closeButton?.addEventListener('click', closeDialog);
    dialog?.addEventListener('click', (event) => {
        if (event.target === dialog) {
            closeDialog();
        }
    });

    dialog?.addEventListener('close', () => {
        document.body.classList.remove('dialog-open');
        if (dialogImage) {
            dialogImage.src = '';
        }
        opener?.focus();
    });

    const year = document.querySelector('#current-year');
    if (year) {
        year.textContent = String(new Date().getFullYear());
    }
})();
