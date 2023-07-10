$(document).ready(function () {
    $('.cpf').mask('000.000.000-00')
    $('.valor').mask('0000,00', { reverse: true })
    $('.saldo').maskMoney({ thousands: '.', decimal: ',', allowZero: true })
    $('.telefone').mask('00 00000-0000')
})