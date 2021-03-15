<script>
  import TextInput from "./TextInput.svelte";
  import Guest from "./Guest.svelte";
  let loading = false;
  let valid = false;
  let success = false;
  let error = null;
  let validationErrors = [];
  let email;
  let emailError;
  let comment;
  let guest;
  let guest1;
  let guest2;

  $: valid = !!(
    [guest, guest1, guest2].find((g) => {
      return g && g.name;
    }) && email
  );

  const getError = (key, errors) => {
    const error = (errors ? errors : []).find((e) => {
      return e.loc[1] === key;
    });
    return error ? error.msg : null;
  };

  $: emailError = getError("email", validationErrors);

  const createResponse = async () => {
    error = null;
    validationErrors = [];
    loading = true;
    try {
      const res = await fetch("/api/responses", {
        method: "POST",
        header: { "content-type": "application/json" },
        body: JSON.stringify({
          email: email,
          comment: comment,
          guests: [guest, guest1, guest2].filter((g) => {
            return g && g.name;
          }),
        }),
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
        return;
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

<div class="text-black">
  <div class="text-4xl mb-8 font-thin tracking-widest">RSVP</div>
  <form>
    {#if success}
      <span>Takk! Hlökkum til að sjá þig</span>
    {:else}
      <div class="mb-6"><Guest label="Nafn" bind:value={guest} /></div>
      <div class="mb-6">
        <Guest label="Nafn maka" bind:value={guest1} />
      </div>
      <div class="mb-8">
        <TextInput
          error={emailError}
          bind:value={email}
          label="Netfang"
          autocapitalize={"off"}
        />
      </div>
      <div class="mb-6">
        <TextInput bind:value={comment} label="Athugasemdir" />
      </div>

      {#if error}
        <span>Eitthvað fór úrskeðis - hringdu í Jökul! 6161339</span>
      {/if}

      <div class="mt-16 sm:mb-0">
        {#if loading}
          <span>Augnablik ...</span>
        {:else}
          <button
            class={`font-bold float-right md:float-none ${
              !valid ? "opacity-50 cursor-default" : ""
            }`}
            disabled={!valid}
            on:click={(event) => {
              event.preventDefault();
              createResponse();
            }}>Senda</button
          >
        {/if}
      </div>
    {/if}
  </form>
</div>
