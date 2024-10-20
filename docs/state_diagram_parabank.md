# State Diagram for Parabank

```mermaid
stateDiagram-v2
    [*] --> Unauthorized: Открытие сайта
    state Unauthorized {
        [*] --> ViewingSite: Нахождение на главной странице
        ViewingSite --> Registration: Нажатие "Register"
        Registration --> Authorized: Успешная регистрация
        Registration --> Registration: Ошибка валидации
        ViewingSite --> Login: Ввод credentials
        Login --> Authorized: Успешный вход
        Login --> Login: Неверные данные
    }
    state Authorized {
        [*] --> AccountOverview: Просмотр счета
        AccountOverview --> OpenAccount: Открытие нового счета
        OpenAccount --> AccountOverview: Счет создан
        OpenAccount --> OpenAccountError: Ошибка при создании счета
        OpenAccountError --> OpenAccount: Попытка повторного создания
        AccountOverview --> TransferFunds: Перевод средств
        TransferFunds --> AccountOverview: Успешный перевод
        TransferFunds --> TransferFundsError: Ошибка перевода
        TransferFundsError --> TransferFunds: Повторить перевод
        AccountOverview --> BillPay: Оплата счетов
        BillPay --> AccountOverview: Успешная оплата
        BillPay --> BillPayError: Ошибка оплаты
        BillPayError --> BillPay: Повторить оплату
        AccountOverview --> RequestLoan: Запрос кредита
        RequestLoan --> AccountOverview: Кредит одобрен
        RequestLoan --> RequestLoanDenied: Кредит отклонен
        RequestLoanDenied --> RequestLoan: Повторная заявка
        AccountOverview --> TransactionHistory: Просмотр истории транзакций
        TransactionHistory --> AccountOverview: Возврат к обзору счета
        AccountOverview --> UpdateContactInfo: Обновление контактной информации
        UpdateContactInfo --> AccountOverview: Информация обновлена успешно
        UpdateContactInfo --> UpdateContactInfoError: Ошибка обновления информации
        UpdateContactInfoError --> UpdateContactInfo: Повторить обновление
        AccountOverview --> Logout: Нажатие "Logout"
    }
    Authorized --> Unauthorized: Выход из системы
```
