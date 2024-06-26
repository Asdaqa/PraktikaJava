const searchForm = document.getElementById('search-form');
const equipmentTable = document.getElementById('equipment-table').querySelector('tbody');

searchForm.addEventListener('submit', (event) => {
  event.preventDefault();

  // Получить данные из формы
  const id = document.getElementById('id').value;
  const name = document.getElementById('name').value;
  const type = document.getElementById('type').value;
  const status = document.getElementById('status').value;

  // Отправить AJAX-запрос на backend
  fetch('/search-equipment', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ id, name, type, status })
  })
  .then(response => response.json()) // Преобразовать ответ в JSON
  .then(data => {
    // Очистить таблицу
    equipmentTable.innerHTML = '';

    // Заполнить таблицу результатами поиска
    data.forEach(equipment => {
      const row = equipmentTable.insertRow();

      const idCell = row.insertCell();
      idCell.textContent = equipment.id;

      const nameCell = row.insertCell();
      nameCell.textContent = equipment.name;

      const typeCell = row.insertCell();
      typeCell.textContent = equipment.type;

      const statusCell = row.insertCell();
      statusCell.textContent = equipment.status;

      const issueDateCell = row.insertCell();
      issueDateCell.textContent = equipment.issueDate;

      const customerCell = row.insertCell();
      customerCell.textContent = equipment.customer;

      // Кнопка "Изменить"
      const editButton = document.createElement('button');
      editButton.textContent = 'Изменить';
      editButton.addEventListener('click', () => {
        // Открыть страницу обновления/удаления, передав ID оборудования
        window.location.href = `update.html?id=${equipment.id}`; 
      });

      // Кнопка "Удалить"
      const deleteButton = document.createElement('button');
      deleteButton.textContent = 'Удалить';
      deleteButton.addEventListener('click', () => {
        if (confirm(`Вы действительно хотите удалить оборудование с ID ${equipment.id}?`)) {
          // Отправить AJAX-запрос на backend для удаления оборудования
          fetch(`/delete-equipment/${equipment.id}`, {
            method: 'DELETE'
          })
          .then(response => {
            if (response.ok) {
              // Обновить таблицу после удаления
              row.remove();
              alert('Оборудование успешно удалено!');
            } else {
              // Обработка ошибки удаления
              return response.json()
                .then(error => {
                  alert('Ошибка при удалении: ' + error.message);
                });
            }
          })
          .catch(error => {
            console.error('Ошибка при отправке запроса:', error);
          });
        }
      });

      // Добавить кнопки в ячейку действий
      const actionsCell = row.insertCell();
      actionsCell.appendChild(editButton);
      actionsCell.appendChild(deleteButton);
    });
  })
  .catch(error => {
    console.error('Ошибка при поиске:', error);
  });
});
