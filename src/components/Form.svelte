<script>
  import TextInput from "./TextInput.svelte";
  import Guest from "./Guest.svelte";
  let loading = false;
  let valid = false;
  let success = false;
  let error = null;
  let validationErrors = [];
  let phone;
  let phoneError;
  let email;
  let emailError;
  let guest;
  let guest1;
  let guest2;

  $: valid = !!(
    [guest, guest1, guest2].find((g) => {
      return g && g.name;
    }) &&
    phone &&
    email
  );

  const getError = (key, errors) => {
    const error = (errors ? errors : []).find((e) => {
      return e.loc[1] === key;
    });
    return error ? error.msg : null;
  };

  $: phoneError = getError("phone", validationErrors);
  $: emailError = getError("email", validationErrors);

  const createResponse = async (data) => {
    error = null;
    validationErrors = [];
    loading = true;
    try {
      const res = await fetch(`/responses`, {
        method: "POST",
        header: { "content-type": "application/json" },
        body: JSON.stringify(data),
      });
      const { status } = res;
      loading = false;
      if (status === 500) {
        error = true;
        return;
      }
      const responseData = await res.json();
      if (status === 422) {
        validationErrors = responseData.detail;
      } else {
        success = true;
      }
      return responseData;
    } catch (error) {
      error = error;
      loading = false;
      return;
    }
  };
</script>

<div class="text-black w-full sm:max-w-md">
  <div class="text-4xl mb-8">RSVP</div>
  <form class="w-full">
    <div class="flex w-full">
      <div class="mb-4 w-28">
        <TextInput error={phoneError} bind:value={phone} label="Sími" />
      </div>
      <div class="mb-8 ml-4 w-40 flex-grow">
        <TextInput
          error={emailError}
          bind:value={email}
          label="Netfang"
          autocapitalize={"off"}
        />
      </div>
    </div>
    <div class="my-4"><Guest label="Nafn" bind:value={guest} /></div>
    <div class="my-4"><Guest label="Nafn +1" bind:value={guest1} /></div>
    <div class="my-4"><Guest label="Nafn +2" bind:value={guest2} /></div>

    {#if error}
      <span>Eitthvað fór úrskeðis - hringdu í Jökul! 6161339</span>
    {/if}

    <div class="my-16 sm:mb-0">
      {#if loading}
        <span>Augnablik ...</span>
      {:else if success}
        <span>Takk! Hlökkum til að sjá þig</span>
      {:else}
        <button
          class={`font-bold ${!valid ? "opacity-50 cursor-default" : ""}`}
          disabled={!valid}
          on:click={(event) => {
            event.preventDefault();
            createResponse({
              phone: phone,
              email: email,
              guests: [guest, guest1, guest2].filter((g) => {
                return g && g.name;
              }),
            });
          }}>Senda</button
        >
      {/if}
    </div>
  </form>
</div>
