<script>
  import TextInput from "./TextInput.svelte";
  import FoodPreference from "./FoodPreference.svelte";

  export let label;
  export let value = { name: undefined, diet: undefined };

  $: if (!value.name) {
    value = { name: undefined, diet: undefined };
  }
</script>

<div class="flex">
  <div class="flex-grow">
    <TextInput {label} bind:value={value.name} autocapitalize={"words"} />
  </div>
  {#if value && value.name}
    <div class="ml-2 w-42">
      <FoodPreference bind:value={value.diet} />
    </div>
  {/if}
</div>
