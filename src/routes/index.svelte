<script context="module">
  export const prerender = true;
</script>

<script>
  import Form from "../components/Form.svelte";
</script>

<svelte:head>
  <title>Jökull ♡ Sunna</title>
  <meta property="og:title" content="Jökull ♡ Sunna" />
  <meta property="og:url" content="https://brudkaup.solberg.is/" />
  <meta
    property="og:image"
    content="https://brudkaup.solberg.is/opengraph.png"
  />
</svelte:head>

<div class="h-screen">
  <div class="min-h-screen">
    <div
      class="w-full min-h-screen flex flex-col md:flex-row justify-center font-serif"
    >
      <div class="m-3 sm:m-6 md:max-w-lg flex flex-col justify-around">
        <div
          class="py-6 px-12 text-center bg-yellow-50 bg-center rounded shadow-xl"
          style="background-image: url(/paper.jpg); background-size: 50%;"
        >
          <div class="text-4xl my-12 font-bold">Jökull & Sunna</div>
          <div>
            <img src="/branch.png" class="inline" width="120" alt="Branch" />
          </div>
          <div class="my-12">
            <p class="mb-2">
              Laugardaginn <span class="italic">28. ágúst 2021</span> munum við
            </p>
            <p class="font-bold mb-2">
              Jökull Sólberg Auðunsson og <br />Sunna Björg Gunnarsdóttir
            </p>

            <p class="mb-2">
              ganga í heilagt hjónaband. Athöfnin mun fara fram í <span
                class="italic">Dómkirkjunni kl 16:30</span
              >. Að lokinni athöfn munum við bjóða til veislu á
              <span class="italic">Kolabrautinni</span> í Hörpu.
            </p>
            <p class="mb-8">
              Það væri okkur sönn ánægja ef þið sæjuð ykkur fært að mæta og
              fagna þessum merkisdegi með okkur.
            </p>
            <p class="mb-8">
              Vinsamlegast staðfestið komu ykkar með því að fylla út RSVP formið
              á þessari síðu.
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
      <div class="m-6 flex flex-col flex-grow md:max-w-xs justify-around">
        <Form />
      </div>
    </div>
  </div>
</div>
