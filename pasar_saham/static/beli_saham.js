if (document.readyState == 'loading'){
    document.addEventListener('DOMContentLoaded', ready)
    // document.getElementsByClassName('saham-quantity-input')[0].value = 1
    // document.getElementsByClassName('saham-total-harga')[0].innerText = 'Rp. 100,000'
} else {
    ready()
    // document.getElementsByClassName('saham-quantity-input')[0].value = 1
    // document.getElementsByClassName('saham-total-harga')[0].innerText = 'Rp. 100,000'
}

function updatePrice(value) {
    if (value === 1) {
        return 'Rp 100.000'
    }
    updateTotalPembelian(value)
    updateImbal(value)
}

function ready() {
    var inputSahamQuantity = document.getElementsByClassName('saham-quantity-input')[0]
    updateTotalPembelian(inputSahamQuantity)
    updateImbal(inputSahamQuantity)
    document.getElementsByClassName('btn-beli-saham')[0].addEventListener('click', beli)
}

function increaseValue() {
    var value = parseInt(document.getElementsByClassName('saham-quantity-input')[0].value);
    value++;
    document.getElementsByClassName('saham-quantity-input')[0].value = value;
    updateTotalPembelian(value)
    updateImbal(value)
}

function decreaseValue() {
    var value = parseInt(document.getElementsByClassName('saham-quantity-input')[0].value);
    if (value > 1){
      value--;
    }
    document.getElementsByClassName('saham-quantity-input')[0].value = value;
    updateTotalPembelian(value)
    updateImbal(value)
}

function beli() {
    // some ajax code to be written here to modify model attribute
    alert('Terima kasih atas transaksi yang dilakukan!')
    document.getElementsByClassName('saham-quantity-input')[0].value = 1
    document.getElementsByClassName('saham-total-harga')[0].innerText = 'Rp. 100,000'
    document.getElementsByClassName('saham-total-imbal-balik')[0].innerText = 'Rp. 7,500'
}

function updateTotalPembelian(value) {
    var totalPembelian = 100000 * value
    document.getElementsByClassName('saham-total-harga')[0].innerText = formatRupiah(totalPembelian, 'Rp. ')
    updateImbal(totalPembelian)
}

function updateImbal(value) {
    var totalImbal = Math.floor(value*0.3/4 * 100000)
    document.getElementsByClassName('saham-total-imbal-balik')[0].innerText = formatRupiah(totalImbal, 'Rp. ')
}

/* Fungsi formatRupiah taken from https://www.malasngoding.com/membuat-format-rupiah-dengan-javascript/ */
function formatRupiah(angka, prefix){
    var number_string = angka.toString().replace(/[^,\d]/g, '').toString(),
    split   		= number_string.split(','),
    sisa     		= split[0].length % 3,
    rupiah     		= split[0].substr(0, sisa),
    ribuan     		= split[0].substr(sisa).match(/\d{3}/gi);

    // tambahkan titik jika yang di input sudah menjadi angka ribuan
    if(ribuan){
        separator = sisa ? ',' : '';
        rupiah += separator + ribuan.join(',');
    }

    rupiah = split[1] != undefined ? rupiah + ',' + split[1] : rupiah;
    return prefix == undefined ? rupiah : (rupiah ? 'Rp. ' + rupiah : '');
}
