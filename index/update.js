const updateForm = document.getElementById('update-form');

// Получить ID оборудования из параметра URL
const urlParams = new URLSearchParams(window.location.search);
const equipmentId = urlParams.get('id');

// Загрузить данные оборудования с backend
fetch(`/get-equipment/${equipmentId}`)
  .then(response => response.json())
  .then(equipment => {
    // Заполнить форму данными оборудования
    document.getElementById('id').value = equipment.id;
    document.getElementById('name').value = equipment.name;
    document.getElementById('type').value = equipment.type;
    document.getElementById('description').value = equipment.description;
    document.getElementById('status').value = equipment.status;
    document.getElementById('issue_date').value = equipment.issueDate;
    document.getElementById('customer').value = equipment.customer;
  })
  .catch(error => {
    console.error('Ошибка при получении данных:', error);
  });

updateForm.addEventListener('submit', (event) => {
  event.preventDefault();

  // Получить обновленные данные из формы
  const id = document.getElementById('id').value;
  const name = document.getElementById('name').value;
  const type = document.getElementById('type').value;
  const description = document.getElementById('description').value;
  const status = document.getElementById('status').value;
  const issueDate = document.getElementById('issue_date').value;
  const customer = document.getElementById('customer').value;

  // Отправить AJAX-запрос на backend для обновления оборудования
  fetch(`/update-equipment/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ id, name, type, description, status, issueDate, customer })
  })
  .then(response => {
    if (response.ok) {
      // Обработка успешного обновления
      alert('Оборудование успешно обновлено!');
      // Перенаправить пользователя на страницу поиска
      window.location.href = 'search.html'; 
    } else {
      // Обработка ошибки
      return response.json()
        .then(error => {
          alert('Ошибка при обновлении: ' + error.message);
        });
    }
  })
  .catch(error => {
    console.error('Ошибка при отправке запроса:', error);
  });
});
