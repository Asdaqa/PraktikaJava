const addEquipmentForm = document.getElementById('add-equipment-form');

addEquipmentForm.addEventListener('submit', (event) => {
  event.preventDefault(); // Предотвратить стандартную отправку формы

  // Получить данные из формы
  const id = document.getElementById('id').value;
  const name = document.getElementById('name').value;
  const type = document.getElementById('type').value;
  const description = document.getElementById('description').value;
  const issueDate = document.getElementById('issue_date').value;
  const customer = document.getElementById('customer').value;

  // Отправить AJAX-запрос на backend
  fetch('/add-equipment', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ id, name, type, description, issueDate, customer })
  })
  .then(response => {
    if (response.ok) {
      // Обработка успешного добавления
      alert('Оборудование успешно добавлено!');
      // Перенаправить пользователя на страницу поиска
      window.location.href = 'search.html';
    } else {
      // Обработка ошибки
      return response.json()
        .then(error => {
          alert('Ошибка при добавлении: ' + error.message);
        });
    }
  })
  .catch(error => {
    console.error('Ошибка при отправке запроса:', error);
  });
});
