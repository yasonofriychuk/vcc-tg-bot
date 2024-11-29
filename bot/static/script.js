// Функция для отображения тоста с ошибкой
function showToast(message) {
    const toast = document.getElementById('toast-danger');
    const toastMessage = document.getElementById('toast-message');

    toast.classList.add('hidden');

    toastMessage.textContent = message;

    setTimeout(() => {
        toast.classList.remove('hidden');
        toast.classList.remove('opacity-0');
        toast.classList.add('opacity-100');
    }, 50);

    setTimeout(() => {
        toast.classList.remove('opacity-100');
        toast.classList.add('opacity-0');
        setTimeout(() => {
            toast.classList.add('hidden');
        }, 500);
    }, 2000);
}