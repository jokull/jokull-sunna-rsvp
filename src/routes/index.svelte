<script>
  import TextInput from "../components/TextInput.svelte";
  const getResponses = async () => {
    await fetch(`${window.location}/responses`);
    return await response.json();
  };
</script>

<svelte:head>
  <title>Jökull ♡ Sunna</title>
</svelte:head>

<div>
  <div
    class="min-h-screen w-full pointer-events-none fixed"
    style="background: no-repeat url(/leaves.png)"
  />
  <div class="min-h-screen flex flex-col md:flex-row justify-center font-serif">
    <div
      class="m-6 md:max-w-lg rounded shadow-xl flex flex-col justify-around"
      style="background: url(/paper.png) center"
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
            ganga í heilagt hjónaband. Athöfnin mun fara fram í Dómkirkjunni kl
            16:30 og strax að lokinni athöfn munum við bjóða til veislu í
            Kolabrautinni, Hörpu.
          </p>
          <p>
            Það væri okkur sönn ánægja ef þú gætir séð þér fært að mæta og fagna
            þessum merkisdegi með okkur.
          </p>
        </div>
      </div>
    </div>

    <div class="m-6 max-w-lg flex flex-col justify-around">
      <div class="text-black">
        <div class="text-4xl mb-8">RSVP</div>
        <form>
          <div class="flex">
            <div class="mb-4 w-28">
              <TextInput label="Sími" small={true} />
            </div>
            <div class="mb-8 ml-4 w-40">
              <TextInput label="Netfang" />
            </div>
          </div>

          <div class="my-4 flex">
            <div class="mt-2 mr-2">
              <TextInput label="Nafn" />
            </div>
            <div class="mt-2">
              <label class="block">
                <span>&nbsp;</span>
                <select class="block w-full mt-1 border-0 bg-transparent">
                  <option>Vegan</option>
                  <option>Fiskur</option>
                  <option>Kjöt</option>
                </select>
              </label>
            </div>
          </div>

          <div class="my-4 flex">
            <div class="mt-2 mr-2">
              <TextInput label="Nafn +1" />
            </div>
            <div class="mt-2">
              <label class="block">
                <span>&nbsp;</span>
                <select class="block w-full mt-1 border-0 bg-transparent">
                  <option>Vegan</option>
                  <option>Fiskur</option>
                  <option>Kjöt</option>
                </select>
              </label>
            </div>
          </div>

          <div class="my-4 flex">
            <div class="mt-2 mr-2">
              <TextInput label="Nafn +2" />
            </div>
            <div class="mt-2">
              <label class="block">
                <span>&nbsp;</span>
                <select class="block w-full mt-1 border-0 bg-transparent">
                  <option>Vegan</option>
                  <option>Fiskur</option>
                  <option>Kjöt</option>
                </select>
              </label>
            </div>
          </div>

          <div class="my-16">
            <button class="font-bold">Senda</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
