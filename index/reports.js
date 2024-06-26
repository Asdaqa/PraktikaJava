const reportForm = document.getElementById('report-form');
const reportTable = document.getElementById('report-table').querySelector('tbody');

reportForm.addEventListener('submit', (event) => {
  event.preventDefault();

  // Получить данные из формы
  const startDate = document.getElementById('start_date').value;
  const endDate = document.getElementById('end_date').value;

  // Отправить AJAX-запрос на backend
  fetch('/generate-report', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ startDate, endDate })
  })
  .then(response => response.json()) // Преобразовать ответ в JSON
  .then(data => {
    // Очистить таблицу
    reportTable.innerHTML = '';

    // Заполнить таблицу отчетом
    data.forEach(equipment => {
      const row = reportTable.insertRow();

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
    });
  })
  .catch(error => {
    console.error('Ошибка при генерации отчета:', error);
  });
});
