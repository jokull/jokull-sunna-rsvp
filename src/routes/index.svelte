<script>
  import Form from "../components/Form.svelte";
</script>

<svelte:head>
  <title>Jökull ♡ Sunna</title>
</svelte:head>

<div class="h-screen">
  <div class="min-h-screen">
    <div
      class="w-full min-h-screen flex flex-col md:flex-row justify-center font-serif"
    >
      <div class="m-3 sm:m-6 md:max-w-lg flex flex-col justify-around ">
        <div
          class="py-6 px-12 text-center bg-yellow-50 bg-center rounded shadow-xl"
          style="background-image: url(/paper.jpg); background-size: 50%;"
        >
          <div class="text-4xl my-12 font-bold">Jökull & Sunna</div>
          <div>
            <img src="/branch.png" class="inline" width="120" alt="Branch" />
          </div>
          <div class="my-12">
            <p class="mb-2">Þann 28. ágúst 2021 munum við</p>
            <p class="font-bold mb-2">
              Jökull Sólberg Auðunsson og <br />Sunna Björg Gunnarsdóttir
            </p>

            <p class="mb-2">
              ganga í heilagt hjónaband. Athöfnin mun fara fram í <span
                class="italic">Dómkirkjunni kl 16:30</span
              >
              og strax að lokinni athöfn munum við bjóða til veislu í
              <span class="italic">Kolabrautinni</span>, Hörpu.
            </p>
            <p class="mb-8">
              Það væri okkur sönn ánægja ef þú gætir séð þér fært að mæta og
              fagna þessum merkisdegi með okkur.
            </p>
            <p class="text-sm font-light">
              Ef einhverjar spurningar vakna vinsamlegast hafðu samband við
              <a class="underline" href="mailto:jokull@solberg.is"
                >jokull@solberg.is</a
              >
              eða
              <a class="underline" href="mailto:sunna@solberg.is"
                >sunna@solberg.is</a
              >
            </p>
          </div>
        </div>
      </div>

      <div class="m-6 flex flex-col justify-around">
        <Form />
      </div>
    </div>
  </div>
</div>
