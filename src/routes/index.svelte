<script>
  import Form from "../components/Form.svelte";
</script>

<svelte:head>
  <title>Jökull ♡ Sunna</title>
</svelte:head>

<div class="h-screen">
  <div class="min-h-screen relative">
    <div
      class="w-full min-h-screen flex flex-col md:flex-row justify-center font-serif"
    >
      <div
        class="m-3 sm:m-6 md:max-w-lg rounded shadow-xl flex flex-col justify-around bg-yellow-50 bg-center"
        style="background-image: url(/paper.png); background-size: 50%;"
      >
        <div class="py-6 px-12 text-center">
          <div class="text-3xl my-12 font-medium">Jökull & Sunna</div>
          <div>
            <img src="/branch.png" class="inline" width="120" alt="Branch" />
          </div>
          <div class="my-12">
            <p class="mb-2">Þann 28. ágúst 2021 munum við</p>
            <p class="font-bold mb-2">
              Jökull Sólberg Auðunsson og <br />Sunna Björg Gunnarsdóttir
            </p>

            <p class="mb-2">
              ganga í heilagt hjónaband. Athöfnin mun fara fram í Dómkirkjunni
              kl 16:30 og strax að lokinni athöfn munum við bjóða til veislu í
              Kolabrautinni, Hörpu.
            </p>
            <p>
              Það væri okkur sönn ánægja ef þú gætir séð þér fært að mæta og
              fagna þessum merkisdegi með okkur.
            </p>
          </div>
        </div>
      </div>

      <div class="m-6 max-w-lg flex flex-col justify-around">
        <Form />
      </div>
    </div>
  </div>
</div>
