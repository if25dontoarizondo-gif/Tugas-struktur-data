<?php

class produk {

//property
public string $kode;
public string $nama;
public int $harga;
public int $stok;

//constan
public const PAJAK = 0.11;
}

//object
$produk = new produk();

$produk->kode = "P001";
$produk->nama = "laptop";
$produk->harga = 10000000;
$produk->stok = 5;

//hitung pajak  
$pajak = produk::PAJAK * 100; //11
$jumlahPajak = $produk->harga * produk::PAJAK; //1.1 juta

//total
$total = $produk->harga + $jumlahPajak; //11.1 juta

//hasil
echo "Produk : " . $produk->nama;
echo "<br/>";

echo "harga : " . $produk->harga;
echo "<br/>";

echo "stok : " . $produk->stok;
echo "<br/>";

echo "pajak: ". $pajak ."%";
echo "<br/>";

echo 'total harga setelah pajak : ' . $total;
echo "<br/>";

